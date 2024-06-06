pip install pillow numpy svgwrite opencv-python   

### Explanation:
1. Preprocessing:

- The image is processed to grayscale, optionally inverted, contrast-enhanced, and then converted to a binary image.
- The binary image is then converted to uint8 type, which is compatible with PBM format.

2. Saving as PBM:

- The binary image is saved as a PBM file, which is the required input format for potrace.

3. Vectorization with Potrace:

- The script calls the potrace command line tool to convert the PBM file to an SVG file.

4. Cleaning Up:

- The temporary PBM files are removed after vectorization.

### Usage
python image2svg.py image.jpeg output_normal.svg output_inverted.svg