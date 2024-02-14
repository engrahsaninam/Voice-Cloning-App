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

# API endpoints
alpha_api_url = "https://futureforge-fastapi-production.up.railway.app/metavoice"
xtts_api_url = "https://futureforge-fastapi-production.up.railway.app/xtts"

# Streamlit App Header with relevant graphic
st.image("logo.png", width=200)
st.title("MetaVoice Text-to-Speech")

# User Input Section
st.header("Enter Text and Input Audio URL")

# Improved styling for input fields
text_input = st.text_area("Text to Convert", "")
audio_input = st.text_input("Input Audio URL", "")

# Dropdown for selecting model
model_selection = st.selectbox("Select Model", ["Alpha", "XTTS"])

# Update API URL based on model selection
api_url = alpha_api_url if model_selection == "Alpha" else xtts_api_url

# Button to Trigger API Request
if st.button("Generate Voice"):
    with st.spinner("Generating Voice..."):
        # Break down the text into pieces of length 150 characters
        text_pieces = [text_input[i:i+150] for i in range(0, len(text_input), 150)]

        # Create a list to store audio file paths
        audio_paths = []

        # Process each text piece using the API
        for i, piece in enumerate(text_pieces):
            payload = {"text": piece, "input_audio": audio_input}
            try:
                response = requests.post(
                    api_url,
                    json=payload,
                    headers={"accept": "application/json", "Content-Type": "application/json"},
                )
                if response.status_code == 200:
                    audio_url = response.json()["audio_url"]

                    # Download the audio file
                    try:
                        response = requests.get(audio_url, stream=True)
                        response.raise_for_status()

                        # Create a temporary file to store the audio data
                        with open(f"temp_audio_{i}.wav", "wb") as f:
                            for chunk in response.iter_content(1024):
                                f.write(chunk)

                        # Append the audio file path to the list
                        audio_paths.append(f"temp_audio_{i}.wav")

                    except requests.exceptions.RequestException as e:
                        st.error(f"Error downloading audio: {e}")
                        break  # Stop processing if an error occurs

                else:
                    st.error(
                        f"Error: {response.status_code}. Please check your input and try again."
                    )
                    break  # Stop processing if an error occurs

            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}. Please try again later.")
                break  # Stop processing if an error occurs

        # Combine audio files into one
        if len(audio_paths) > 0:
            combined_audio_path = "combined_audio.wav"
            os.system(f"sox {' '.join(audio_paths)} {combined_audio_path}")

            # Play the combined audio using Streamlit
            st.audio(combined_audio_path)

            # Remove temporary audio files
            for path in audio_paths:
                try:
                    os.remove(path)
                except OSError:
                    pass
