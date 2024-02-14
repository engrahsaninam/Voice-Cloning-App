import streamlit as st
import requests
import os

# Set Streamlit theme to light with a gradient
st.set_page_config(
    page_title="MetaVoice TTS",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Set background gradient
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #85D8CE, #4A77AF);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# API endpoint URL
api_url = "https://futureforge-fastapi-production.up.railway.app/metavoice"

# Streamlit App Header with relevant graphic
st.image("logo.png", width=200)
st.title("MetaVoice Text-to-Speech")

# User Input Section
st.header("Enter Text and Input Audio URL")

# Improved styling for input fields
text_input = st.text_area("Text to Convert", "")
audio_input = st.text_input("Input Audio URL", "")

# Button to Trigger API Request
if st.button("Generate Voice"):
    with st.spinner("Generating Voice..."):
        # API Request Payload
        payload = {"text": text_input, "input_audio": audio_input}

        # API Request
        try:
            response = requests.post(
                api_url,
                json=payload,
                headers={"accept": "application/json", "Content-Type": "application/json"},
            )
            if response.status_code == 200:
                audio_url = response.json()["audio_url"]  # Extract the audio URL from the response

                # Download the audio file
                try:
                    response = requests.get(
                        audio_url, stream=True
                    )  # Stream the download for efficiency
                    response.raise_for_status()  # Raise an exception for error status codes

                    # Create a temporary file to store the audio data
                    with st.empty():
                        with open("temp_audio.wav", "wb") as f:
                            for chunk in response.iter_content(1024):
                                f.write(chunk)

                    # Play the audio using Streamlit
                    st.audio("temp_audio.wav")

                except requests.exceptions.RequestException as e:
                    st.error(f"Error downloading audio: {e}")

                # Remove the temporary file (optional)
                try:
                    os.remove("temp_audio.wav")
                except OSError:
                    pass  # Ignore errors if the file doesn't exist
            else:
                st.error(
                    f"Error: {response.status_code}. Please check your input and try again."
                )
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}. Please try again later.")
