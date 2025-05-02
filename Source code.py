import os
import psutil
import random
import openai
import pyttsx3
import datetime
import time
import speech_recognition as sr
import webbrowser
import subprocess

# Set your OpenAI API key (you need to get an API key from OpenAI)
openai.api_key = 'your-openai-api-key'

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio).lower()
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("There was an issue with the speech recognition service.")
            return None

def open_application(command):
    applications = {
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "whatsapp": "C:\\Users\\YourUsername\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
        "file explorer": "explorer",
        "weather": "ms-weather:",
        "youtube": "https://www.youtube.com/"
    }
    
    for app in applications:
        if app in command:
            if applications[app].startswith("http"):
                webbrowser.open(applications[app])
            else:
                os.system(f'start "" "{applications[app]}"')
            speak(f"Opening {app}")
            return
    
    speak("Sorry, I couldn't find the application.")

def web_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Here are the search results for {query}")

def assistant_loop():
    speak("Hello boss, how can I assist you?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "bye" in command:
                speak("Goodbye boss, have a great day!")
                break
            elif "open" in command:
                open_application(command)
            else:
                web_search(command)

def greet_user():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "Good morning boss!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon boss!"
    else:
        greeting = "Good evening boss!"

    welcome_message = f"Welcome! {greeting} I am your Assistant."
    speak(welcome_message)
    print(welcome_message)

def scan_and_protect():
    greet_user()
    assistant_loop()

if __name__ == "__main__":
    scan_and_protect()
