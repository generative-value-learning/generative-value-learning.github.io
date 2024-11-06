#!/bin/bash

# Create output directories if they don't exist
mkdir -p converted

# Function to process a single video
process_video() {
    local input_file="$1"
    local dirname=$(dirname "$input_file")
    local basename=$(basename "$input_file" .webm)
    local output_file="converted/${dirname}/${basename}.mp4"
    
    # Create subdirectory in converted folder
    mkdir -p "converted/${dirname}"
    
    # Get video dimensions
    local dimensions=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$input_file")
    local width=$(echo $dimensions | cut -d'x' -f1)
    local height=$(echo $dimensions | cut -d'x' -f2)
    
    # Calculate new height (75% of original) and offset
    local new_height=$((height * 3 / 4))
    local crop_offset=$((height / 4))
    
    echo "Converting and cropping: $input_file"
    
    # Convert and crop the video, without audio
    ffmpeg -i "$input_file" \
           -vf "crop=$width:$new_height:0:$crop_offset" \
           -c:v libx264 \
           -preset medium \
           -profile:v baseline \
           -level 3.0 \
           -movflags +faststart \
           -pix_fmt yuv420p \
           -an \
           "$output_file" \
           -y
}

# Process all webm files
for video in */*.webm; do
    if [ -f "$video" ]; then
        process_video "$video"
    fi
done

echo "Conversion complete! Files are in the 'converted' directory"
