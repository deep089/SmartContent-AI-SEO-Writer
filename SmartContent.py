import streamlit as st
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

hf_token = "Your_API_KEY"

 # Load environment variables from .env
hf_token = os.getenv("HUGGINGFACE_API_KEY")

if not hf_token:
 raise ValueError("HUGGINGFACE_API_KEY not found. Please check your .env file.")



generator = pipeline(
"text-generation",
 model="Qwen/Qwen2.5-1.5B-Instruct",
   framework="pt"
)


# Streamlit UI
st.set_page_config(page_title="SEO Content Generator", layout="centered")
st.title("🔍 AI-Powered SEO Content Generator")

# --- Input Fields ---
keyword = st.text_input("🔑 Target Keyword", placeholder="e.g., kitchen remodeling in Miami")
content_type = st.selectbox("📄 Content Type", ["Blog Post", "Product Description", "Service Page"])
tone = st.selectbox("🗣️ Tone", ["Professional", "Casual", "Persuasive", "Helpful"])
length = st.slider("✍️ Desired Word Count", min_value=300, max_value=1500, value=600, step=100)

if st.button("Generate Content"):
    if not keyword:
        st.warning("Please enter a keyword.")
    else:
        with st.spinner("Generating SEO content..."):
            prompt = f"""
You are an SEO expert and professional content writer. Write a {length}-word {content_type.lower()} targeting the keyword "{keyword}".
Use proper H1, H2, and H3 headings.
Ensure keyword density is between 1% and 2%.
Tone of writing should be {tone.lower()}.
The content should be engaging, informative, and well-structured.
Conclude with a call to action.
Do not repeat sentences. Maintain a natural flow.
            """

            try:
                output = generator(prompt, max_new_tokens=length * 2, temperature=0.7)[0]["generated_text"]
                st.subheader("📄 Generated Content")
                st.markdown(output)
            except Exception as e:
                st.error(f"Error: {e}")
