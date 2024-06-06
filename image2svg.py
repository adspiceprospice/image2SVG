import sys
import numpy as np
from PIL import Image, ImageOps
import cv2
import subprocess
import os

def preprocess_image(image_path, invert=False):
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    
    if invert:
        # Invert the image (so the logo is black and the background is white)
        image = ImageOps.invert(image)
    
    # Enhance contrast
    contrast_image = ImageOps.autocontrast(image, cutoff=0)
    
    # Convert the image to a binary image (black and white)
    binary_image = contrast_image.point(lambda p: p > 128 and 255).convert('1')
    
    # Convert the binary image to uint8
    binary_image = np.array(binary_image, dtype=np.uint8) * 255
    
    return binary_image

def save_pbm(binary_image, pbm_path):
    # Save the binary image as PBM file
    pil_image = Image.fromarray(binary_image)
    pil_image.save(pbm_path, 'PPM')

def convert_pbm_to_svg(pbm_path, svg_path):
    # Use potrace to convert PBM to SVG
    subprocess.run(['potrace', pbm_path, '-s', '-o', svg_path])

def process_image(image_path, output_normal_path, output_inverted_path):
    # Process and save normal image
    normal_image = preprocess_image(image_path, invert=False)
    normal_pbm_path = 'temp_normal.pbm'
    save_pbm(normal_image, normal_pbm_path)
    convert_pbm_to_svg(normal_pbm_path, output_normal_path)
    os.remove(normal_pbm_path)
    
    # Process and save inverted image
    inverted_image = preprocess_image(image_path, invert=True)
    inverted_pbm_path = 'temp_inverted.pbm'
    save_pbm(inverted_image, inverted_pbm_path)
    convert_pbm_to_svg(inverted_pbm_path, output_inverted_path)
    os.remove(inverted_pbm_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python convert_image_to_svg.py input.png output_normal.svg output_inverted.svg")
    else:
        input_path = sys.argv[1]
        output_normal_path = sys.argv[2]
        output_inverted_path = sys.argv[3]
        
        process_image(input_path, output_normal_path, output_inverted_path)
