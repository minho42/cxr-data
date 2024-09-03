import os
import shutil

# Define the source directory and the target directory
source_directory = os.path.expanduser('~/Desktop/NIH Chest X-rays')
target_directory = os.path.join(source_directory, 'all_images')

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Loop through the subdirectories to find images in the 'images' folder
for subdir in os.listdir(source_directory):
    subdir_path = os.path.join(source_directory, subdir)
    
    # Only proceed if the item is a directory and has an 'images' subdirectory
    if os.path.isdir(subdir_path):
        images_path = os.path.join(subdir_path, 'images')
        if os.path.exists(images_path) and os.path.isdir(images_path):
            for image_file in os.listdir(images_path):
                image_path = os.path.join(images_path, image_file)
                
                # Only copy files (ignore directories)
                if os.path.isfile(image_path):
                    try:
                        shutil.copy(image_path, target_directory)
                        print(f"Copied: {image_path} to {target_directory}")
                    except Exception as e:
                        print(f"Error copying {image_path}: {e}")

print(f"All images have been copied to {target_directory}")
