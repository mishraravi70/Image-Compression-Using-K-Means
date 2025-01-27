

# Image Compression Using K-Means

This project demonstrates an interactive web application for image compression using the K-Means clustering algorithm. The app is built using [Streamlit](https://streamlit.io/) and allows users to compress images by reducing the number of colors and adjusting the file size.

## Features

- Upload images in `.jpg`, `.jpeg`, or `.png` formats.
- Compress images by reducing the number of colors using K-Means clustering.
- Adjust the output image to a target file size (in KB).
- Preview the original and compressed images.
- Download the compressed image.

## Installation

To run the application locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python dependencies:
   ```bash
   pip install streamlit numpy scikit-learn pillow opencv-python
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application by running the command above.
2. Upload an image file using the file uploader.
3. Choose the number of colors (K) for compression using the slider.
4. Enter the desired target size in KB.
5. Click the **Compress Image** button to compress the image.
6. View the compressed image preview and download the image if satisfied.

## Adding an Image to README

You can add an image to this README file by using the following Markdown syntax:

```markdown
![Alt text](relative-path-to-image "Optional title")
```

For example, to add a screenshot of the app:

```markdown
![App Screenshot](assets/app_screenshot.png "Streamlit App Screenshot")
```

Ensure the image file is placed in the appropriate directory within the repository.

## Code Explanation

### Core Functions

1. **Image Compression Using K-Means**:
   - The function `compress_image_kmeans()` reduces the number of colors in the image by clustering similar colors together.
   - Each pixel is replaced by the centroid of its respective cluster.

2. **Size Adjustment**:
   - The function `save_and_resize_to_target()` ensures the compressed image meets the desired size by iteratively adjusting the JPEG quality.

### Streamlit Integration

- The app uses Streamlit's components like `st.file_uploader`, `st.slider`, and `st.number_input` for user interaction.
- `st.image` is used to display the uploaded and compressed images.
- `st.download_button` provides a way to download the compressed image.

## Example

Here is an example of how the app looks when running:

![App Screenshot](assets/app_screenshot.png "Streamlit App Screenshot")

## Files

- **app.py**: Main application file containing the Streamlit app and core functions.
- **assets/**: Folder to store any supporting images (e.g., screenshots).

## Dependencies

- Python 
- Streamlit
- NumPy
- scikit-learn
- Pillow
- OpenCV

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

## License

This project is licensed under the [MIT License](LICENSE).




