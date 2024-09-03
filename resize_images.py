import pandas as pd
from PIL import Image
import os

# Read the CSV file and extract the 'name' column without the .jpg extension
df = pd.read_csv('data2.csv')
image_names_from_csv = set(df['name'].str.replace('.jpg', ''))  # Keep names without the extension

# Define source and target directories
source_directory = os.path.expanduser('./all_images')
target_directory = os.path.join(os.path.dirname(source_directory), 'resized_images')

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Set the target size and quality
max_size = (512, 512)  # Resize to a maximum width and height of 512 pixels (adjust as needed)
quality = 85  # Quality setting for JPEG format (1-100)

# Loop through all the images in the source directory
for image_file in os.listdir(source_directory):
    image_path = os.path.join(source_directory, image_file)
    
    # Process only image files
    if os.path.isfile(image_path):
        # Extract the name without the extension
        image_name_without_ext = os.path.splitext(image_file)[0]

        # Check if the image name (without extension) is in the CSV list
        if image_name_without_ext in image_names_from_csv:
            try:
                # Open the image file
                with Image.open(image_path) as img:
                    # Resize the image while maintaining aspect ratio
                    img.thumbnail(max_size, Image.LANCZOS)

                    # Convert to RGB if needed (some formats may need conversion to save as JPEG)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Save the resized image to the target directory with JPEG format
                    target_path = os.path.join(target_directory, f"{image_name_without_ext}.jpg")
                    img.save(target_path, format="JPEG", quality=quality)
                    
                    print(f"Resized and saved: {target_path}")

                # Remove the processed image name from the list for efficiency
                image_names_from_csv.remove(image_name_without_ext)

            except Exception as e:
                print(f"Error processing {image_path}: {e}")

print(f"All matching images have been resized and saved to {target_directory}")
