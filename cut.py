import os
from PIL import Image

def resize_images_in_folder(folder_path, width, height):
    # Create an output directory
    output_folder = os.path.join(folder_path, "resized")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        try:
            with Image.open(file_path) as img:
                # Resize the image
                img_resized = img.resize((width, height))
                
                # Save the resized image in the output folder
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)
                print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Skipped file {filename}: {e}")

# Example usage
folder_path = "C:/Users/Jan Held/ConvexeSplatting/3DCS/assets/comparisons"  # Replace with the path to your folder
resize_images_in_folder(folder_path, 980, 545)
