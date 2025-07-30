import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os
import musicLibrary  
# ------------ API KEY SETUP --------------
# Register at newsapi.org for your own free key (current key works for demos)
NEWSAPI_KEY = "0b63ad04cd9c4bd6a6fbe897fc37836a"

# ------------ VOICE ENGINE SETUP --------------
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text, slow=False):
    """Convert text to speech and play it."""
    print("Jarvis:", text)
    tts = gTTS(text, lang='en', slow=slow)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def google_search(query):
    """Open a new Google search for the given query and announce it."""
    speak(f"Searching Google for {query}")
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)

def processCommand(c):
    """Process voice commands and perform appropriate actions."""
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        try:
            # If you have a musicLibrary.py, you can use your personal library
            from musicLibrary import music
            if song in music:
                link = music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Playing {song} from YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        except ImportError:
            speak(f"Playing {song} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif "news" in c:
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI_KEY}"
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])[:5]
                if not articles:
                    speak("Sorry, I couldn't find any news today.")
                for article in articles:
                    speak(article['title'])
            else:
                speak("Sorry, failed to fetch news.")
        except Exception as ex:
            speak(f"Error fetching news: {ex}")
    else:
        google_search(c)

def listen_for_wake_word(r, wake_word="jarvis"):
    """Continuously listen for the wake word."""
    with sr.Microphone() as source:
        print("Listening for wake word...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=2)
                said = ""
                try:
                    said = r.recognize_google(audio).lower()
                    print(f"Heard: {said}")
                except sr.UnknownValueError:
                    continue
                if wake_word in said:
                    return
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    r = sr.Recognizer()
    while True:
        listen_for_wake_word(r)
        speak("Yes?")
        with sr.Microphone() as source:
            print("Jarvis Active...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            try:
                command = r.recognize_google(audio)
                print("You said:", command)
                processCommand(command)
            except Exception as e:
                print("Error:", e)
