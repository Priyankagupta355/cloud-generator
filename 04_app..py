import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# App Title
st.title("🌥 Word Cloud Generator")
st.write("Upload your text or type it in the box below and generate a word cloud!")

# Text input
text_input = st.text_area("Enter text here", "Type or paste your text...")

# Upload file option
uploaded_file = st.file_uploader("Or upload a text file (.txt)", type=["txt"])

if uploaded_file is not None:
    # Read uploaded file
    text_input = uploaded_file.read().decode('utf-8')

# Generate Word Cloud button
if st.button("Generate Word Cloud"):
    if text_input.strip() == "":
        st.warning("⚠ Please enter some text or upload a file first!")
    else:
        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_input)
        
        # Display the word cloud
        plt.figure(figsize=(15, 7))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)