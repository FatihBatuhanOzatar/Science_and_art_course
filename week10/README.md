# Week 10: Prompt Optimization & Creativity Tests

This directory contains the experiments and results for Week 10. The objective was to analyze the impact of hyperparameters (temperature) and prompt engineering on Generative AI outputs using the Hugging Face Inference API.

## Experiment 1: Temperature Parameter (Text Generation)
I tested the **Mistral-7B** model with different `temperature` settings to observe the variance in creativity and randomness.

**Prompt:** *"Once upon a time, a robot fell in love with a toaster. The story continues..."*

### Result A: Low Temperature (0.1)
*(Observation: The model produces deterministic, repetitive, and strictly logical text.)*
> **Output:** [PASTE YOUR LOW TEMPERATURE OUTPUT HERE]

### Result B: High Temperature (0.9)
*(Observation: The model becomes more diverse, creative, and less predictable.)*
> **Output:** [PASTE YOUR HIGH TEMPERATURE OUTPUT HERE]

---

## Experiment 2: Prompt Engineering (Image Generation)
I compared a basic prompt against an optimized, descriptive prompt using **Stable Diffusion XL**.

### Prompt Comparison
* **Simple Prompt:** *"A cat."*
* **Optimized Prompt:** *"A majestic fluffy cat wearing a king's crown, sitting on a velvet throne, cinematic lighting, 8k resolution, hyper-realistic, fantasy style."*

### Visual Results
The image below demonstrates the significant difference in quality and style adherence.

![Comparison Result](comparison_result.png)
*(Note: This image was generated using the Week 10 Notebook)*

## Conclusion
* **Text Generation:** Lower temperatures are suitable for factual tasks (coding, definitions), while higher temperatures are essential for creative writing to avoid repetition.
* **Image Generation:** Detailed prompts containing keywords related to lighting, texture, and style significantly improve the quality and artistic value of the generated images compared to simple one-word prompts.
