# DeepFake-AI-detection
This Python program is designed to help users detect whether an audio file is real or a potential deepfake. By utilizing audio feature extraction and comparing the results against preset thresholds, the tool gives a quick and user-friendly way to assess audio authenticity. Here's a brief explanation of how the program works.
#Features of the Tool
1) Graphical User Interface (GUI):
Built using the Tkinter library, the program has a simple window where users can upload an audio file for analysis.
Users can click a button to select a .wav file from their system, and the result of the analysis is displayed directly in the application window.

2) Audio Feature Extraction:
The program uses Librosa, a powerful audio analysis library, to extract key features from the uploaded audio file.
Two audio features are extracted for analysis:
MFCCs (Mel-frequency cepstral coefficients): These capture the important characteristics of the sound, often used in voice recognition and audio classification.
Spectral Centroid: This indicates the center of mass of the sound's spectrum, which is useful in determining the brightness of the sound.

3) Deepfake Detection Logic:
The program applies a simple decision-making process based on the extracted features.
It uses predefined threshold values to check if the audio is likely to be a deepfake.
If the mean MFCCs or spectral centroid values exceed certain thresholds, the audio is flagged as a possible deepfake.

# How It Works
1) Upload the Audio:
The user selects an audio file by clicking on the "Attach Audio" button in the GUI.

2) Extract Audio Features:
Once a file is selected, the program extracts the MFCCs and spectral centroid of the audio file.

3) Deepfake Detection:
The extracted features are then compared against preset thresholds.
If the audio exceeds these thresholds, the tool suggests that it "may be a deepfake." Otherwise, it indicates that "the audio seems to be real."

4) Display the Result:
The result is displayed in the window, providing the user with a quick evaluation of the audio's authenticity.
