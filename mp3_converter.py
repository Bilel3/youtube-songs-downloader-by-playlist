import os
import subprocess

def convert_to_mp3(input_file, output_file):
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', output_file])
        print(f"Conversion successful: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to MP3: {e}")

def convert_all_files(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.mp4', '.webm')):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.mp3')
            convert_to_mp3(input_file_path, output_file_path)

if __name__ == "__main__":
    input_directory = "downloads/done"  # Replace with the path to your input directory
    output_directory = "downloads/converted"  # Replace with the desired path for the output directory

    convert_all_files(input_directory, output_directory)
