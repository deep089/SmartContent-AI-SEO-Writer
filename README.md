# SmartContent-AI-SEO-Writer

## Introduction
SEO Optimizer AI is a Streamlit-based web application that leverages open-source language models from Hugging Face to generate SEO-optimized content. It allows users to input a target keyword, choose a tone, content type, and desired word count to produce high-quality, structured, and engaging content tailored for search engine visibility.

## Features
- Generate SEO-friendly content with customizable parameters
- Supports multiple content types: Blog Post, Product Description, Service Page
- Adjustable tone: Professional, Casual, Persuasive, Helpful
- Word count range: 300 to 1500 words
- Utilizes Hugging Face open-source models (e.g., Zephyr, Qwen, Mistral)

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/seo-optimizer-ai.git
   cd seo-optimizer-ai

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file and add your Hugging Face API key:
   HUGGINGFACE_API_KEY=your_token_here

5. Run the app:
   streamlit run SEO_Optimizer.py

## Usage
1. Enter a target keyword.
2. Select the content type and tone.
3. Choose the desired word count.
4. Click "Generate Content" to receive SEO-optimized text.

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- dotenv
- PyTorch

