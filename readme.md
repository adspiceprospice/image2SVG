pip install pillow numpy potrace


### Explanation:
Preprocess the Image:

- Convert the image to grayscale to simplify the data.
- Invert the image to ensure that the logo is black and the background is white, which is more suitable for the tracing process.
- Enhance the contrast to make the edges of the logo more distinct.
- Convert the image to a binary image (black and white) to remove any residual grayscale values, ensuring a clean transition between the logo and the background.
- Convert the Preprocessed Image:

Use the potrace library to convert the preprocessed image to a bitmap.
- Trace the bitmap to generate the vector path.
- Write the vector path data to an SVG file.
