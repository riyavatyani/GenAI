import streamlit as st
import pandas as pd 
import time
from google import genai

def generate_poetry(prompt):
    if prompt:
        msg = st.toast("Gathering inspiration...")
        time.sleep(2)
        msg = st.toast("Writing poetry...")
        time.sleep(2)
        msg = st.toast("Poem is ready!", icon="✍️")
        time.sleep(2)

        st.write(f"So you want a poem about {prompt}.")
        time.sleep(1)
        st.write("Here’s something beautiful for you:")

        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a short beautiful poem about {prompt}"
        )

        st.write(response.text)


if __name__ == "__main__":
    API_KEY = "AIzaSyAkR52CA8A-XgbFx1CZ0oj43d45NjU5xkk"   # Replace with new key
    client = genai.Client(api_key=API_KEY)

    st.title("Poetry Generator ✨")
    prompt = st.chat_input("What should I write a poem about?")
    generate_poetry(prompt)
