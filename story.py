import streamlit as st
import pandas as pd 
import time
from google import genai

def generate_story(prompt):
    if prompt:
        msg = st.toast("Walking through the hills...")
        time.sleep(2)
        msg = st.toast("Listening to the wind...")
        time.sleep(2)
        msg = st.toast("Story is ready!", icon="🌿")
        time.sleep(2)

        st.write(f"So you want a story about {prompt}.")
        time.sleep(1)
        st.write("Let me tell you a gentle tale...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                "Write a short nostalgic story inspired by Ruskin Bond. Use simple language, nature imagery, and emotional warmth."
            ]
        )

        st.write(response.text)


if __name__ == "__main__":
    API_KEY = "AIzaSyAkR52CA8A-XgbFx1CZ0oj43d45NjU5xkk"   # Put new regenerated key
    client = genai.Client(api_key=API_KEY)

    st.title("🌿 Storytelling Bot")
    prompt = st.chat_input("What should the story be about?")
    generate_story(prompt)
