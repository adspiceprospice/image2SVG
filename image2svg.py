import sys
import numpy as np
from PIL import Image, ImageOps
import svgwrite
from skimage import io, color, filters, measure

def preprocess_image(image_path):
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    
    # Invert the image (so the logo is black and the background is white)
    inverted_image = ImageOps.invert(image)
    
    # Enhance contrast
    contrast_image = ImageOps.autocontrast(inverted_image, cutoff=0)
    
    # Convert the image to a binary image (black and white)
    binary_image = contrast_image.point(lambda p: p > 128 and 255).convert('1')
    
    # Convert the binary image to uint8
    binary_image = np.array(binary_image, dtype=np.uint8) * 255
    
    return binary_image

def convert_image_to_svg(image_path, svg_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)

    # Use scikit-image to find contours
    contours = measure.find_contours(processed_image, level=128)
    
    # Create an SVG drawing
    height, width = processed_image.shape
    dwg = svgwrite.Drawing(svg_path, size=(width, height))
    
    # Add contours to the SVG
    for contour in contours:
        points = [(float(point[1]), float(point[0])) for point in contour]  # Note the (y, x) to (x, y) conversion
        dwg.add(dwg.polyline(points, stroke='black', fill='none'))
    
    # Save the SVG file
    dwg.save()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert_image_to_svg.py input.png output.svg")
    else:
        convert_image_to_svg(sys.argv[1], sys.argv[2])
