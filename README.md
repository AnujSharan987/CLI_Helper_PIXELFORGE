# ⚡ GemTerm

> An ultra-fast, AI-powered developer CLI to debug, generate, and fix code without ever leaving your terminal.

GemTerm bridges the gap between your command-line workflow and the intelligence of the Gemini API. Instead of context-switching to a browser when debugging or scaffolding scripts, GemTerm reads your files, queries Gemini directly from your terminal, displays formatted markdown analysis, and lets you write fixed code with a single keystroke.

---

## ✨ Features

* **Terminal-Native Workflow:** Debug and generate code without leaving Vim, Neovim, Bash, or PowerShell.
* **Smart Code Correction:** Reads existing files, identifies bugs, outputs the fix, and prompts you to save the corrected version (`filename_corrected.ext`).
* **Scaffolding from Scratch:** Specify a new filename and a prompt to instantly generate complete, working scripts.
* **Rich Markdown Output:** Beautiful syntax highlighting and formatted terminal panels powered by `rich`.
* **Zero Overhead Setup:** Use the pre-built standalone binary or run directly via Python.

---

## 🚀 Quickstart

### Option 1: Standalone Binary (No Python required)
1. Download `gemterm.exe` from the [Latest Releases](https://github.com/AnujSharan987/CLI_Helper_PIXELFORGE/releases/tag/v1.0.0).
2. Move `gemterm.exe` to a folder included in your system `PATH` (e.g., `C:\tools`).
3. Run `gemterm` from any terminal.

### Option 2: Run with Python

1. Clone the repository:
   git clone https://github.com/AnujSharan987/CLI_Helper_PIXELFORGE.git
   cd CLI_Helper_PIXELFORGE

2. Install dependencies:
   pip install google-genai rich pyinstaller

3. Set API Key:
   # PowerShell
   $env:GEMINI_API_KEY="your_api_key_here"

   # Linux / macOS
   export GEMINI_API_KEY="your_api_key_here"

*(Note: If not set as an environment variable, GemTerm will prompt you for it directly upon execution).*

---

## 💻 Usage & Commands

### 1. Fix Bugs in an Existing File
Point GemTerm to any existing code file with your prompt:

python gemterm.py buggy_code.py "find why this crashes and fix it"

GemTerm inspects your file, explains the issue, displays the corrected code, and prompts:
Save updated code to buggy_code_corrected.py? (y/n): y

### 2. Generate a Brand New Script
Specify a target filename that does not exist yet:

python gemterm.py snake_game.py "create a complete playable snake game using pygame"

### 3. Using with the Standalone Binary (.exe)
If you downloaded `gemterm.exe` and added it to your system PATH:

gemterm script.py "refactor this function for better time complexity"

---
[View on GitHub](https://github.com/AnujSharan987/CLI_Helper_PIXELFORGE)

## 📄 License

This project is open-source under the [MIT License](LICENSE).
