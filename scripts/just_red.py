
"""
Note:
    This code was generated from ChatGPT being told to rewrite main.go of the original project.
"""
import os
import sys
from PIL import Image

# Import functions from ../../libs/image_utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../libs")))
from image_utils import remove_green_channel, remove_blue_channel, save_image

def process_image(file_path):
    try:
        # Open the image
        img = Image.open(file_path)
        img = img.convert("RGBA")  # Ensure the image has an alpha channel

        # Remove green and blue channels
        no_green = remove_green_channel(img)
        no_green_blue = remove_blue_channel(no_green)

        # Save the processed image
        output_path = f"{os.path.splitext(file_path)[0]}.no-GB.png"
        save_image(no_green_blue, output_path)

    except Exception as e:
        print(f"Failed to process image {file_path}: {e}")

def main():
    if len(sys.argv) <= 1:
        print("Usage: python just_red.py path/to-image.png")
        return

    # Process each provided file path
    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f"Invalid file path: {file_path}")
            continue

        process_image(file_path)

if __name__ == "__main__":
    main()