import tkinter as tk
from tkinter import filedialog
import librosa
import numpy as np

def extract_audio_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)
    
    
    mfccs_mean = np.mean(mfccs, axis=1)
    spectral_centroid_mean = np.mean(spectral_centroid)

    return mfccs_mean, spectral_centroid_mean

def is_deepfake(mfccs_mean, spectral_centroid_mean):
   
    mfcc_threshold = 100  
    spectral_centroid_threshold = 2000  

   
    return (mfccs_mean > mfcc_threshold).any() or (spectral_centroid_mean > spectral_centroid_threshold)

def process_audio():
    audio_file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio files", "*.wav")])

    if audio_file_path:
        mfccs_mean, spectral_centroid_mean = extract_audio_features(audio_file_path)
        result = is_deepfake(mfccs_mean, spectral_centroid_mean)

        output_label.config(text="The audio may be a deepfake." if result else "The audio seems to be real.")

# GUI setup
root = tk.Tk()
root.title("Deepfake Audio Detection")

# Title
title_label = tk.Label(root, text="Deepfake Audio Detection", font=("Helvetica", 16))
title_label.pack(pady=10)

# Insert Audio Text
insert_audio_label = tk.Label(root, text="Insert the Audio", font=("Helvetica", 12))
insert_audio_label.pack(pady=5)

# Button to attach audio file
attach_button = tk.Button(root, text="Attach Audio", command=process_audio)
attach_button.pack(pady=10)

# Output box
output_label = tk.Label(root, text="", font=("Helvetica", 12))
output_label.pack(pady=10)

# Run the GUI
root.mainloop()