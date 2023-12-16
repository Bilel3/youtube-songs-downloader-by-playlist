import os
import shutil

def replace_with_mp3(src_folder, dest_folder, converted_folder):
    for root, _, files in os.walk(src_folder):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            if os.path.splitext(file_path)[1].lower() != '.mp3':
                # Find the corresponding MP3 file in the "converted" folder
                mp3_filename = os.path.splitext(filename)[0] + '.mp3'
                mp3_path = os.path.join(converted_folder, mp3_filename)

                if os.path.exists(mp3_path):
                    # Copy the MP3 file to the "new" subfolder
                    dest_path = os.path.join(dest_folder, os.path.relpath(file_path, src_folder))
                    dest_path_mp3 = os.path.splitext(dest_path)[0] + '.mp3'
                    
                    shutil.copy2(mp3_path, dest_path_mp3)
                    print(f"Replaced {filename} with {mp3_filename} in {os.path.relpath(root, src_folder)}")

                    # Remove non-MP3 files in the "new" subfolder
                    for file in os.listdir(root):
                        file_full_path = os.path.join(root, file)
                        if os.path.isfile(file_full_path) and os.path.splitext(file_full_path)[1].lower() != '.mp3':
                            os.remove(file_full_path)
                            print(f"Removed non-MP3 file: {file} in {os.path.relpath(root, src_folder)}")

if __name__ == "__main__":
    new_folder = "downloads/new"  # Replace with the path to your "new" directory
    converted_folder = "downloads/converted"  # Replace with the path to your "converted" directory

    replace_with_mp3(new_folder, new_folder, converted_folder)
