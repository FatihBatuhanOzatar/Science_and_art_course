# 🚀 Science & Art: GenAI Final Project (Week 12)

This repository contains the final version of the Generative AI Term Project.
The application integrates a Large Language Model (Mistral-7B) and a Text-to-Image Model (SDXL) into a single, cohesive interface with post-processing capabilities.

## 🔗 Live Demo
**👉 [Click Here to Try the App Live!](LINK_HERE)**

## ✨ Features
1.  **AI Chatbot:** Powered by `Mistral-7B-Instruct`, capable of coding assistance, creative writing, and logic.
2.  **Art Generator:** Powered by `Stable Diffusion XL`, generating high-quality images from text prompts.
3.  **Image Filters:** Integrated `Pillow` library to apply real-time filters (Grayscale, Contour, Blur) to generated images.
4.  **Secure Deployment:** Uses Streamlit Secrets management to handle API keys securely without exposing them in the code.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Engine:** Hugging Face Inference API
* **Image Processing:** Pillow (PIL)
* **Deployment:** Streamlit Cloud

## 📂 Project Structure
* `app.py`: The main application source code.
* `requirements.txt`: List of dependencies for cloud deployment.
