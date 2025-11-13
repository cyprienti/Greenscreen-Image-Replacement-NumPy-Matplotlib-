# Greenscreen-Image-Replacement
This project implements a simple greenscreen background replacement using only NumPy and Matplotlib. It loads two images — a person in front of a green screen and a forest background — as NumPy arrays, removes the green background, and combines the person with the forest image.

# Features
  -  Green pixel detection and masking using NumPy.
  -  Background replacement with a new image using element-wise operations.
  -  Visualization of each processing step using Matplotlib.
  -  Saves a PNG file (person_in_forest.png) containing all stages side by side.

# How to Run
  -  Download and extract the provided ZIP archive.
  -  Open a terminal in the project folder.

# Install dependencies:

    pip install -r requirements.txt

# Run the script:

    python greenscreen_replace.py

The output image person_in_forest.png will be generated in the same directory.


# Output

The resulting person_in_forest.png will contain:
  -  The original image (with green background)
  -  The image after background removal

The final composite (person in forest)

 # Implementation Notes

  Only NumPy and Matplotlib are allowed.
  Do not use libraries such as OpenCV or PIL.

  Green pixel detection can be done using a logical mask, for example:

    green_mask = (image[:, :, 1] > 100) & (image[:, :, 0] < 100) & (image[:, :, 2] < 100)

Use NumPy array indexing to combine the person and forest images.

 # Learning Objectives

  -  Understand how digital images can be represented as NumPy arrays.
  -  Practice element-wise array manipulation and logical masking.
  -  Visualize intermediate processing steps with Matplotlib.
