import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image, ImageFilter, ImageOps
import io

st.set_page_config(page_title="GenAI Final Project", layout="wide", page_icon="🚀")

# Canlı yayında token'ı 'secrets'tan alır.
# GitHub'a şifre yüklemyiz
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
except:
    st.error("Error: Hugging Face Token not found. Please add it to Streamlit Secrets.")
    st.stop()

# --- MODELS ---
CHAT_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
ART_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

st.title("🚀 Science & Art: GenAI Final Project")
st.markdown("### Interactive AI Playground: Chat & Art Generation")
st.markdown("Powered by **Mistral-7B** and **SDXL** via Hugging Face API.")

# Initialize Client
client = InferenceClient(token=HF_TOKEN)


# --- HELPER: FILTERS ---
def apply_filter(image, filter_type):
    if filter_type == "Grayscale":
        return ImageOps.grayscale(image)
    elif filter_type == "Blur":
        return image.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_type == "Contour":
        return image.filter(ImageFilter.CONTOUR)
    elif filter_type == "Invert":
        return ImageOps.invert(image)
    elif filter_type == "Sharpen":
        return image.filter(ImageFilter.SHARPEN)
    return image


# --- SIDEBAR ---
mode = st.sidebar.radio("Navigation:", ["💬 AI Chatbot", "🎨 Art Studio"])

# --- CHAT MODE ---
if mode == "💬 AI Chatbot":
    st.header("💬 Chat with Mistral-7B")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am ready to help with science, code, or creative writing."}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = ""
                stream = client.chat_completion(
                    [{"role": "user", "content": prompt}],
                    model=CHAT_MODEL,
                    max_tokens=500,
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        response += chunk.choices[0].delta.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"API Error: {e}")

# --- ART MODE ---
elif mode == "🎨 Art Studio":
    st.header("🎨 AI Art Generator (SDXL)")

    if "generated_image" not in st.session_state:
        st.session_state.generated_image = None

    with st.form("art_form"):
        prompt = st.text_input("Describe your imagination:", "Astronaut riding a horse on Mars, realistic, 4k")
        submit = st.form_submit_button("Generate Art")

    if submit and prompt:
        with st.spinner("Creating masterpiece... (This may take a few seconds)"):
            try:
                image = client.text_to_image(prompt, model=ART_MODEL)
                st.session_state.generated_image = image
            except Exception as e:
                st.error(f"Generation Error: {e}")

    if st.session_state.generated_image:
        st.subheader("Post-Processing Studio")
        col1, col2 = st.columns(2)

        with col1:
            st.image(st.session_state.generated_image, caption="Original AI Output", use_container_width=True)

        with col2:
            filter_choice = st.selectbox("Apply Filter:",
                                         ["Original", "Grayscale", "Blur", "Contour", "Invert", "Sharpen"])
            filtered_img = apply_filter(st.session_state.generated_image, filter_choice)
            st.image(filtered_img, caption=f"Effect: {filter_choice}", use_container_width=True)

            # Download
            buf = io.BytesIO()
            filtered_img.save(buf, format="PNG")
            st.download_button("Download Image", data=buf.getvalue(), file_name="ai_art.png", mime="image/png")