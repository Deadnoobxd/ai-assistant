 import pyttsx3
import speech_recognition as sr
import pyautogui
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Timeout added
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"Command: {command}")
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return None
        except Exception as e:
            print("Sorry, I couldn't understand that.")
            return None
    return command.lower()

def perform_action(command):
    if "search on google" in command:
        query = command.replace("search on google", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching {query} on Google.")
    
    elif "search on youtube" in command or "play" in command:
        query = command.replace("search on youtube", "").replace("play", "").strip()
        speak(f"Playing {query} on YouTube.")
        pywhatkit.playonyt(query)  # This will search and play the video on YouTube.
    
    elif "brightness up" in command:
        pyautogui.hotkey("fn", "f7")
        speak("Brightness increased.")
    
    elif "brightness down" in command:
        pyautogui.hotkey("fn", "f6")
        speak("Brightness decreased.")
    
    elif "volume up" in command:
        pyautogui.press("volumeup", presses=5)
        speak("Volume increased.")
    
    elif "volume down" in command:
        pyautogui.press("volumedown", presses=5)
        speak("Volume decreased.")
    
    elif "minimize" in command:
        pyautogui.hotkey("win", "down")
        speak("Window minimized.")
    
    elif "maximize" in command:
        pyautogui.hotkey("win", "up")
        speak("Window maximized.")
    
    elif "close" in command:
        pyautogui.hotkey("alt", "f4")
        speak("Window closed.")
    
    elif "pause video" in command:
        pyautogui.press("space")
        speak("Video paused.")
    
    elif "play video" in command:
        pyautogui.press("space")
        speak("Video playing.")
    
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    
    elif "lock" in command:
        speak("Locking the system.")
        pyautogui.hotkey("win", "l")
    else:
        speak("I didn't understand the command.")

# Main loop
if __name__ == "__main__":
    speak("AI Assistant is now active.")
    while True:
        command = take_command()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            perform_action(command)
