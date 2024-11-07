#!/usr/bin/env python3
import os
import sys

def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    # Get directory of index_template.html
    template_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load template file
    template_path = os.path.join(template_dir, 'index_template.html')
    with open(template_path, 'r') as f:
        template = f.read()
        
    # Load component files
    gemini_path = os.path.join(template_dir, 'gemini.html')
    frame_viewer_path = os.path.join(template_dir, 'json-frame-viewer.html')
    
    gemini_content = load_file(gemini_path)
    frame_viewer_content = load_file(frame_viewer_path)
    
    # Replace placeholders
    output = template.replace('[[online-demo]]', gemini_content)
    output = output.replace('[[frame-viewer]]', frame_viewer_content)
    
    # Write output file
    output_path = os.path.join(template_dir, 'index.html')
    with open(output_path, 'w') as f:
        f.write(output)
        
if __name__ == '__main__':
    main()