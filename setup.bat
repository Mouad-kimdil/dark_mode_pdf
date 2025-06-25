@echo off
echo 🌙 PDF Dark Mode Converter Setup
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python first.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv pdf_dark_env

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call pdf_dark_env\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install required packages
echo 📥 Installing dependencies...
pip install PyMuPDF

REM Create requirements.txt
echo 📝 Creating requirements.txt...
echo PyMuPDF>=1.23.0 > requirements.txt

echo.
echo ✅ Setup completed successfully!
echo.
echo 🚀 Starting PDF Dark Mode Converter...
echo.
python dark.py
echo.
echo To run again later:
echo 1. Activate the virtual environment: pdf_dark_env\Scripts\activate.bat
echo 2. Run the converter: python dark.py
echo 3. Deactivate when done: deactivate
echo.
pause