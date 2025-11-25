import os
from pydub import AudioSegment

inbase = "/path/to/your/files" 

# Gathering all wma files
wma_files = []

for root, dirs, files in os.walk(inbase):
    for file in files:
        if file.lower().endswith(".wma"):
            wma_path = os.path.join(root, file)
            wma_files.append(wma_path)

failed_files = [] # Empty list for failed conversions

# File conversion
for wma_path in wma_files:
    filename = os.path.splitext(os.path.basename(wma_path))[0]
    mp3_path = os.path.join(os.path.dirname(wma_path), f"{filename}.mp3")
    
    if os.path.exists(mp3_path):
        print(f"Skipping {mp3_path}: it already exists")
        continue

    try:
        print(f"Converting: {wma_path} → {mp3_path}")
        AudioSegment.from_file(wma_path).export(mp3_path, format="mp3")
    except Exception as e:
        print(f"Failed to convert {wma_path}: {e}")
        failed_files.append(wma_path)
        continue


print(f"There were {len(failed_files)} files that failed.")
