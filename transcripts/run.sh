#!/bin/bash

# Exit on error
set -e

echo "Checking required files..."

# Check for requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found"
    echo "Please create a requirements.txt file with the required dependencies."
    exit 1
fi

# Check for transcripts.py
if [ ! -f "transcripts.py" ]; then
    echo "❌ Error: transcripts.py not found"
    echo "Please ensure transcripts.py exists in this directory."
    exit 1
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found"
    echo ""
    echo "Please create a .env file with your API keys:"
    echo "  1. Copy the example: cp env.example .env"
    echo "  2. Edit .env and add your keys:"
    echo "     - API_KEY (YouTube Data API v3)"
    echo "     - OPENAI_API_KEY (OpenAI API)"
    echo ""
    echo "See README.md for instructions on getting API keys."
    exit 1
fi

echo "✅ All required files present"
echo ""

echo "Setting up Python virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "Running transcripts.py..."
python3 transcripts.py

echo ""
echo "✅ Done!"

