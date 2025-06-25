#!/bin/bash

# PDF Dark Mode Converter Setup Script
echo "🌙 PDF Dark Mode Converter Setup"
echo "================================"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv pdf_dark_env

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source pdf_dark_env/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "📥 Installing dependencies..."
pip install PyMuPDF

# Create requirements.txt
echo "📝 Creating requirements.txt..."
cat >requirements.txt <<EOF
PyMuPDF>=1.23.0
EOF

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "🚀 Starting PDF Dark Mode Converter..."
echo ""
python dark.py
echo ""
echo "To run again later:"
echo "1. Activate the virtual environment: source pdf_dark_env/bin/activate"
echo "2. Run the converter: python dark.py"
echo "3. Deactivate when done: deactivate"

