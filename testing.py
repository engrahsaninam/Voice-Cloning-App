
import librosa
import numpy as np
import soundfile as sf

# Define the input file paths
input_filepath_list =["temp_audio_0.wav", "temp_audio_1.wav", "temp_audio_2.wav"]

# Define the output file path
output_filepath = "combined_audio.wav"
# Load the audio files
audio_list = [sf.read(filepath) for filepath in input_filepath_list]
samplerate=audio_list[0][1]
audio_list=[audio[0] for audio in audio_list]
# Concatenate the audio files
concatenated_audio = np.concatenate(audio_list)

# Save the concatenated audio to a new file
sf.write(output_filepath, concatenated_audio, samplerate=samplerate)