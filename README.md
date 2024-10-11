# PACER

**PACER** is a simple and powerful tool that collects all important code files and configuration files from your project directory and outputs them as a unified text block. It skips auto-generated files and irrelevant content, focusing only on handwritten code and essential configurations.

## Features

- Collects code and configuration files
- Ignores auto-generated and binary files
- Outputs files with clear markers (`<begin>`, `<end>`)
- Multi-platform support (Windows, Linux, macOS)

## How It Works

- **Supported files**: Source code files (`.py`, `.js`, `.java`, etc.) and common configuration formats (`.yaml`, `.json`, `.ini`, etc.).
- **Excluded files**: Binary files (`.exe`, `.dll`, `.log`, `.tmp`, etc.) and directories such as `node_modules`, `build`, and `__pycache__`.

---

## Installation

### Requirements

- Python 3.6 or higher

### How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/codesnap.git
   ```

2. Navigate to the project directory:

   ```bash
   cd <your project path>
   ```

3. Run the script

   ```
   python <path>/collect_files.py 
   ```
