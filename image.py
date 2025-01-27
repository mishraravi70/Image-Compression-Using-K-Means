import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
from io import BytesIO
from PIL import Image
import os

# Function to compress an image using K-Means
def compress_image_kmeans(image, n_colors):
    # Convert image to RGB if it's not already
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2RGB)

    # Reshape image to a 2D array of pixels
    pixel_values = img.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixel_values)

    # Replace each pixel with its corresponding cluster center
    compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
    compressed_pixels = np.clip(compressed_pixels.astype('uint8'), 0, 255)

    # Reshape back to the original image shape
    compressed_image = compressed_pixels.reshape(img.shape)
    return compressed_image

# Function to save image and check its size
def save_and_resize_to_target(compressed_image, target_size_kb):
    # Save compressed image to a buffer
    buffer = BytesIO()
    image = Image.fromarray(compressed_image)
    quality = 95  # Start with high quality
    image.save(buffer, format="JPEG", quality=quality)
    buffer_size_kb = len(buffer.getvalue()) / 1024

    # Adjust quality to meet the target size
    while buffer_size_kb > target_size_kb and quality > 10:
        buffer = BytesIO()
        quality -= 5
        image.save(buffer, format="JPEG", quality=quality)
        buffer_size_kb = len(buffer.getvalue()) / 1024

    return buffer.getvalue(), buffer_size_kb

# Streamlit app
st.title("Image Compression Using K-Means")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    # Select number of colors for compression
    n_colors = st.slider("Number of colors (K)", min_value=2, max_value=128, value=16)

    # Input desired size in KB
    target_size_kb = st.number_input("Target size (KB)", min_value=10, max_value=5000, value=200, step=10)

    if st.button("Compress Image"):
        # Compress image using K-Means
        compressed_image = compress_image_kmeans(image, n_colors)

        # Save and resize to meet target size
        compressed_data, final_size_kb = save_and_resize_to_target(compressed_image, target_size_kb)

        # Display compressed image and details
        st.image(compressed_image, caption=f"Compressed Image ({final_size_kb:.2f} KB)", use_container_width=True)
        st.success(f"Compression successful! Final size: {final_size_kb:.2f} KB")

        # Download button for the compressed image
        st.download_button(
            label="Download Compressed Image",
            data=compressed_data,
            file_name="compressed_image.jpg",
            mime="image/jpeg",
        )
