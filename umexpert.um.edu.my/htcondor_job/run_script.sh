#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_file> <output_file>"
  exit 1
fi

# Assign arguments to variables
INPUT_FILE="$1"
OUTPUT_FILE="$2"

# Path to the virtual environment
VENV_PATH="/mnt/beegfs/crawlerEnv"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Check if activation was successful
if [[ "$VIRTUAL_ENV" != "" ]]; then
  echo "Virtual environment activated."
else
  echo "Failed to activate virtual environment."
  exit 1
fi

# Run the Python script with the provided arguments
python3 /mnt/beegfs/scrape.py "$INPUT_FILE" "$OUTPUT_FILE"

# Deactivate the virtual environment
deactivate
