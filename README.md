# Image Caption Generator

A user-friendly web app that lets users upload images and generates descriptive captions using the BLIP AI model from Hugging Face. The app offers multiple caption options and features an easy-to-use interface built with Streamlit. Ideal for showcasing AI-powered image understanding in an interactive way.

## Features

- Upload images (jpg, jpeg, png)
- Generate up to 3 descriptive captions per image
- Powered by the BLIP model from Hugging Face transformers
- Simple and clean UI built with Streamlit
- Fast inference with cached model loading

## Installation

1. Clone this repository:


git clone https://github.com/Gauravs1714/image-caption-generator.git

2. Change directory:
cd image-caption-generator

3. Install required Python packages:
pip install streamlit torch torchvision transformers pillow

## Usage

Run the app with:
streamlit run image_caption_app.py


Open your browser when prompted, upload an image, and generate captions.

## Project Structure

- `image_caption_app.py`: Main Streamlit app script
- `caption.jpg`: Logo image file used as favicon and app banner (replace with your own)
- `README.md`: Project documentation

## Notes

- The first run may take some time as the BLIP model downloads.
- You can customize the app by modifying the code in `image_caption_app.py`.

## License

This project is licensed under the MIT License.

---

Made with ❤️ using Streamlit and the BLIP model from Hugging Face.
