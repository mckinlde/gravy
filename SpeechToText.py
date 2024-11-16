import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

def record_audio(filename, duration=5, samplerate=44100):
    """Record audio from the microphone and save it as a WAV file."""
    print("Recording...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    sf.write(filename, audio, samplerate)
    print(f"Recording saved to {filename}")

def transcribe_audio(filename, output_textfile):
    """Transcribe audio from a file and save the transcription to a text file."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print("Transcribing...")
        audio = recognizer.record(source)  # Read the audio file
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcription: {text}")
            
            # Save the transcription to a text file
            with open(output_textfile, "w") as file:
                file.write(text)
            print(f"Transcription saved to {output_textfile}")
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"API error: {e}")

# Record audio and save transcription
record_audio("output.wav", duration=5)  # Record for 5 seconds
transcribe_audio("output.wav", "transcription.txt")