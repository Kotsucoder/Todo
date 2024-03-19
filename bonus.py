import streamlit as st
from PIL import Image


def grayscale(image):
    img = Image.open(image)
    gray_img = img.convert("L")
    st.image(gray_img)


uploaded_image = st.file_uploader("Upload Image", key="upload")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    grayscale(camera_image)
if uploaded_image:
    grayscale(st.session_state["upload"])

st.session_state