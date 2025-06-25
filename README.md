# 🌙 PDF Dark Mode Converter

Convert any PDF to dark mode with smart color inversion that preserves text readability.

## Features

- **Interactive Setup**: Prompts for PDF path and output location
- **Smart Color Inversion**: Preserves text readability while creating dark backgrounds
- **Quality Control**: Adjustable brightness and contrast settings
- **High Resolution**: 2x zoom processing for better quality
- **Memory Efficient**: Optimized for large PDFs
- **Cross-Platform**: Works on macOS, Linux, and Windows

## Quick Start

### 1. Setup (First Time Only)

**macOS/Linux:**
```bash
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

### 2. Run the Converter

**Activate virtual environment:**
```bash
# macOS/Linux
source pdf_dark_env/bin/activate

# Windows
pdf_dark_env\Scripts\activate.bat
```

**Run the converter:**
```bash
python dark.py
```

### 3. Follow the Prompts

1. Enter the path to your PDF file
2. Choose where to save the dark mode version
3. Adjust quality settings (optional)
4. Wait for conversion to complete

## Advanced Usage

### Quality Settings

- **Background Brightness** (0.1-0.3): How dark the background should be
  - 0.1 = Very dark (better for OLED screens)
  - 0.3 = Lighter dark (better for LCD screens)

- **Text Contrast** (1.0-2.0): How bright the text should be
  - 1.0 = Normal contrast
  - 2.0 = High contrast (better readability)

### Tips for Best Results

- Use **0.15 brightness** and **1.2 contrast** for most PDFs
- For text-heavy documents, try **0.1 brightness** and **1.5 contrast**
- For documents with images, use **0.2 brightness** and **1.0 contrast**

## Requirements

- Python 3.6+
- PyMuPDF (automatically installed by setup script)

## Troubleshooting

**"File not found" error:**
- Make sure the PDF path is correct
- Use quotes around paths with spaces

**"Permission denied" error:**
- Make sure you have write permissions to the output directory
- Try saving to a different location

**Memory issues with large PDFs:**
- Close other applications
- Process smaller PDFs in batches

## Deactivate Virtual Environment

When you're done:
```bash
deactivate
```