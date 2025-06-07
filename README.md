# Nexa-voice-assistant
Voice activate Virtual assistant
## Project Overview

Nexa performs the following tasks:

- Listens for a wake word ("Nexa")
- Recognizes and processes spoken commands
- Opens popular websites (Google, YouTube, Facebook, etc.)
- Plays songs from a predefined music library
- Fetches and reads news headlines via NewsAPI
- Uses OpenAI to answer general questions and execute intelligent responses

This project demonstrates practical applications of voice control, API integration, and intelligent automation.

---

## Features

| Feature                  | Description                                                                          |
|--------------------------|--------------------------------------------------------------------------------------|
| Voice Recognition        | Converts microphone input to text using SpeechRecognition                           |
| Text-to-Speech (TTS)     | Converts responses to speech using gTTS and plays audio using pygame                |
| Web Automation           | Opens web pages like Google, YouTube, LinkedIn, etc.                                 |
| Music Playback           | Plays music by mapping song keywords to URLs in a music dictionary                  |
| News Updates             | Fetches and speaks top headlines using the NewsAPI                                  |
| AI Query Response        | Sends custom queries to OpenAI GPT-3.5-Turbo and speaks back the response           |

---

## Technologies Used

- Python 3.10+
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [pygame (audio playback)](https://pypi.org/project/pygame/)
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- [NewsAPI](https://newsapi.org/)
- pyttsx3 (optional fallback TTS engine)

---

## Project Structure

Nexa/
── main.py # Main control script
── musicLibrary.py # Dictionary of song names and YouTube URLs
── client.py # (Optional) OpenAI interaction module
── README.md # Project documentation
── requirements.txt # Python dependencies
── venv/ # Python virtual environment (excluded in GitHub)

