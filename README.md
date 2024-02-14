# MetaVoice TTS: Text-to-Speech with Voice Style Transfer

This Streamlit application leverages the MetaVoice API to enable you to convert text into speech, adding the option to incorporate a specific voice style using an input audio URL.

## Features

- **Text-to-Speech:** Enter your text and instantly hear it spoken aloud.
- **Voice Style Transfer:** Apply the voice style from an input audio URL to your generated speech.
- **User-Friendly Interface:** Intuitive input fields and a clear button guide you through the process.
- **Visual Appeal:** Modern and visually appealing design enhances the user experience.

## Getting Started

1. **Install Requirements:** Ensure you have the necessary Python libraries installed. Run `pip install -r requirements.txt` in your terminal.
2. **Obtain API Key:** If you haven't already, head over to https://futureforge-fastapi-production.up.railway.app/metavoice and request an API key.
3. **Update Configuration:** Replace the placeholder API key value (`"YOUR_API_KEY"`) in the code with your actual key.
4. **Run the App:** Execute `streamlit run app.py` in your terminal.
5. **Enter Text and Audio URL:** Type your desired text and provide the URL of an audio file containing the voice style you want to transfer.
6. **Click "Generate Voice":** Hear your text spoken with the transferred voice style!

## Usage Example

**Scenario:** Imagine you want to create a video narration with a specific speaker's voice, but their recording doesn't match the video's tone. Use MetaVoice TTS to transfer the desired voice style from a short audio clip of the speaker to your narrated text, resulting in a seamless and consistent voice throughout the video.

## Requirements

- Python 3.7+
- streamlit >= 1.17.1
- requests >= 2.28.1
- os (included in standard Python library)

## GitHub Repository

This project is hosted on GitHub at https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/remembering-your-github-username-or-email. Feel free to contribute, suggest improvements, or raise issues through pull requests and discussions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, please reach out to engrahsaninam@gmail.com.
