import speech_recognition as sr
import pyttsx3
import re

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def clean_move_text(raw_text):
    text = raw_text.lower()

    number_words = {
        "one": "1", "two": "2", "t o":"to",  
        "three": "3", "four": "4", "for": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8"
    }

    for word, digit in number_words.items():
        text = re.sub(rf"\b{word}\b", digit, text)

    text = text.replace(" ", "")  

    match = re.search(r'([a-h][1-8]).*?([a-h][1-8])', text)
    if match:
        from_sq, to_sq = match.groups()
        return f"{from_sq} to {to_sq}"
    return ""

def listen_for_move():
    with sr.Microphone() as source:
        print("🎤 Listening for your move (e.g., 'move b1 to c2')...")
        speak("Please say your move. For example, move b one to c two.")
        audio = recognizer.listen(source)

        try:
            raw_text = recognizer.recognize_google(audio).lower()
            print(f"🗣 Raw voice input: {raw_text}")
            cleaned_move = clean_move_text(raw_text)
            if cleaned_move:
                speak(f"You said: {cleaned_move}. Do you want to make this move?")
                return cleaned_move
            else:
                speak("I didn't catch a valid move. Please try again.")
                return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            speak("Error connecting to the recognition service.")
            return None

def confirm_move():
    with sr.Microphone() as source:
        print("🟡 Waiting for confirmation (yes or no)...")
        audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio).lower()
            print(f"✅ Confirmation response: {response}")
            return 'yes' in response
        except:
            speak("Couldn't understand confirmation. Try again.")
            return False
def recognize_voice():
    with sr.Microphone() as source:
        print("Listening...")
        speak("Your move. Please say something.")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech service.")
        return ""