# WMA-to-MP3 Batch Converter

This Python script scans a base directory (including all subfolders) for .wma audio files and automatically converts them to .mp3 using **pydub** and **ffmpeg**. Very much a vibe-coded project.

## How it Works
1. Recursively walks through the target folder.  
2. Collects all .wma files.  
3. For each file:
   - Skips conversion if an .mp3 version already exists.  
   - Attempts to convert the .wma file to .mp3.  
   - Records any files that fail.

At the end, the script prints how many conversions failed so you can review or retry them.

## Requirements
- Python 3  
- pydub
- ffmpeg installed and accessible in your system PATH  

## Usage
Update the 'inbase' variable with the path to your music folder, then run the script.

