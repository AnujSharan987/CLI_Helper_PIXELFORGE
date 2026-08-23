import argparse
import os
import re
import sys
from google import genai
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def extract_code_block(response_text: str) -> str:
    """Extracts the first code block if present; otherwise returns raw text."""
    pattern = r"```(?:\w+)?\n([\s\S]*?)```"
    match = re.search(pattern, response_text)
    if match:
        return match.group(1).strip()
    return response_text.strip()

def main():
    parser = argparse.ArgumentParser(
        description="GemTerm: AI developer assistant inside your terminal."
    )
    parser.add_argument("filename", help="Target file path (existing or to be created)")
    parser.add_argument("prompt", help="Instruction or prompt for Gemini")
    parser.add_argument(
        "--model", 
        default="gemini-3.6-flash", 
        help="Gemini model to use (default: gemini-3.6-flash)"
    )

    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = console.input("[yellow]GEMINI_API_KEY not found in environment. Enter your key: [/yellow]").strip()
        if not api_key:
            console.print("[bold red]Error:[/bold red] An API key is required to proceed.")
            sys.exit(1)

    client = genai.Client(api_key=api_key)
    file_exists = os.path.exists(args.filename)
    
    file_content = ""
    if file_exists:
        with open(args.filename, "r", encoding="utf-8") as f:
            file_content = f.read()

    # System instruction & prompt construction
    if file_exists:
        system_instruction = (
            "You are an expert programming assistant in a terminal environment. "
            "When asked to fix or modify code, provide a brief clear explanation, "
            "followed by the complete updated source code enclosed in triple backticks."
        )
        full_query = (
            f"File: {args.filename}\n\n"
            f"--- EXISTING CODE ---\n{file_content}\n--- END CODE ---\n\n"
            f"User Prompt: {args.prompt}"
        )
    else:
        system_instruction = (
            "You are an expert programming assistant in a terminal environment. "
            "Generate clean, fully functioning code based on the user's prompt. "
            "Enclose the primary source code in triple backticks."
        )
        full_query = f"Create a new file `{args.filename}` satisfying this request: {args.prompt}"

    console.print(Panel(f"[bold cyan]Querying Gemini ({args.model})...[/bold cyan]\n[dim]Target: {args.filename}[/dim]"))

    try:
        response = client.models.generate_content(
            model=args.model,
            contents=full_query,
            config={"system_instruction": system_instruction}
        )
    except Exception as e:
        console.print(f"[bold red]API Error:[/bold red] {e}")
        sys.exit(1)

    generated_text = response.text
    console.print("\n" + "="*50 + "\n")
    console.print(Markdown(generated_text))
    console.print("\n" + "="*50 + "\n")

    # Offer file creation/saving
    extracted_code = extract_code_block(generated_text)

    if file_exists:
        base, ext = os.path.splitext(args.filename)
        output_filename = f"{base}_corrected{ext}"
        prompt_text = f"Save updated code to [bold yellow]{output_filename}[/bold yellow]? (y/n): "
    else:
        output_filename = args.filename
        prompt_text = f"Save generated code to [bold yellow]{output_filename}[/bold yellow]? (y/n): "

    choice = console.input(prompt_text).strip().lower()
    if choice in ['y', 'yes']:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(extracted_code)
        console.print(f"[bold green]✓ Successfully written to {output_filename}[/bold green]")
    else:
        console.print("[dim]No files modified.[/dim]")

if __name__ == "__main__":
    main()
