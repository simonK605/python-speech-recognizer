import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Reading Audio file as source
harvard = sr.AudioFile('audios/harvard.wav')


def recognize(audio):
    # Listening the file.
    with audio as source:
        audio = r.record(source)

    try:
        # Recognize speech using Google Web Speech API
        text = r.recognize_google(audio)
        print("Speech detected. Text:", text)
        return 1  # Speech detected
    except sr.UnknownValueError:
        print("No speech detected.")
        return 0  # No speech detected
    except sr.RequestError as e:
        print(f"Error with the API request; {e}")
        return -1  # Error with API request


print(recognize(harvard))
