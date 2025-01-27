# Image-Compression-Using-K-Means
# Image Compression Using K-Means

This Streamlit app allows you to upload an image, compress it using K-Means clustering, and adjust its size to a specified target size in kilobytes (KB). The compression process reduces the number of colors in the image to make it more efficient for storage while maintaining as much visual quality as possible.

## Features

- **Upload an image**: Choose an image in JPG, JPEG, or PNG format.
- **Select number of colors for compression**: Use the slider to select the number of colors (clusters) you want to use for compression, ranging from 2 to 128.
- **Set target size**: Input a desired target size for the compressed image in kilobytes (KB).
- **Compression**: The app applies K-Means clustering to compress the image and reduces its size by modifying the number of colors in the image.
- **Download the compressed image**: After compression, you can download the resulting image in JPEG format.

## How it works

1. **Image Upload**: The user uploads an image via the file uploader.
2. **Color Compression with K-Means**: The image is compressed using the K-Means algorithm, reducing the number of colors.
3. **Size Adjustment**: The compressed image is saved, and its quality is adjusted to meet the target file size, ensuring that the size doesn't exceed the desired KB.
4. **Download**: The user can then download the compressed image in JPEG format.

## Requirements

To run this app locally, ensure you have the following Python packages installed:

- `streamlit`
- `numpy`
- `opencv-python`
- `scikit-learn`
- `Pillow`

You can install them using pip:

```bash
pip install streamlit numpy opencv-python scikit-learn Pillow
Usage
Clone this repository or copy the script into your local environment.
Run the Streamlit app:
bash
Copy
Edit
streamlit run app.py
Open your browser and follow the instructions to upload an image, select the compression parameters, and download the compressed result.
Workflow Diagram
Below is an illustration of the app's workflow:


Let me know if you'd like to add any specific details or further instructions!

vbnet
Copy
Edit

For the workflow image, you can add the image to your GitHub repository and link it with the `path_to_your_workflow_image` URL or path where the image is stored in the repository.

Let me know if you'd like help creating the workflow image!
