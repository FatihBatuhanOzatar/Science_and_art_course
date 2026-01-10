# Week 9: Cloud-Powered Combined GenAI App

This directory contains the deliverables for the Week 9 assignment.

## Task Summary

The objective for this week was to merge the previously developed tools into a single, unified web application.
To ensure high performance and stability on Google Colab's free tier, the architecture was optimized to use **cloud-based inference** instead of local execution.

**Key Achievements:**
* **Unified Interface:** Developed a single Streamlit app (`app.py`) with a sidebar to switch between "Chat Mode" and "Art Mode".
* **Cloud Inference Engine:** Integrated **Hugging Face Inference API** to run heavy models remotely, resolving local GPU memory (VRAM) limitations.
* **Models Used:**
    * **Chat:** `mistralai/Mistral-7B-Instruct-v0.2` (State-of-the-art open LLM).
    * **Art:** `stabilityai/stable-diffusion-xl-base-1.0` (High-quality image generation).

## Deliverables

* **`Week9_Cloud_App.ipynb`:** The Colab notebook used for setup and deployment via Cloudflare Tunnel.
* **`app.py`:** The source code for the Streamlit application.
* **Screenshots:** Evidence of the working application (see below).

## Application Demo

### 1. Chat Mode
<img width="1583" height="818" alt="Ekran görüntüsü 2026-01-10 193958" src="https://github.com/user-attachments/assets/78b72daa-5a0e-46d1-8b53-af77673d1f6d" />


### 2. Art Mode
<img width="692" height="784" alt="Ekran görüntüsü 2026-01-10 194406" src="https://github.com/user-attachments/assets/d4ea7fb6-573c-4268-8f52-3204c2dfd01c" />


## Technical Note: Why Cloud API?
Attempting to load both Mistral-7B and SDXL simultaneously on a free T4 GPU caused frequent "Out of Memory" crashes. By switching to the Hugging Face Inference Client, the application now runs smoothly with zero local resource strain, delivering faster results and higher quality outputs.
