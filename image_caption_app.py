import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

st.set_page_config(
    page_title="Image Caption Generator",
    page_icon=r"C:\Users\gaura\Downloads\caption.jpg",
    layout="centered"
)

logo_image = Image.open(r"C:\Users\gaura\Downloads\caption.jpg")
st.image(logo_image, width=120)

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
    return processor, model

processor, model = load_model()

st.title("🖼️ Image Caption Generator")
st.write("Upload an image, and generate multiple captions describing it.")

uploaded_file = st.file_uploader("Choose an image file (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Captions"):
        with st.spinner("Generating captions..."):
            inputs = processor(image, return_tensors="pt")
            outputs = model.generate(
                **inputs,
                num_beams=5,
                num_return_sequences=3,
                early_stopping=True
            )
            captions = [processor.decode(output, skip_special_tokens=True) for output in outputs]
            st.success("Captions generated!")
            for i, caption in enumerate(captions, 1):
                st.markdown(f"### Caption {i}:\n> {caption}")

else:
    st.info("Please upload an image file to get started.")

st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io) and the [BLIP model](https://huggingface.co/Salesforce/blip-image-captioning-base).")
