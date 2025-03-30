import pyttsx3
import speech_recognition as sr
import pyautogui
import webbrowser
import os
import pywhatkit
import keyboard
import time
import psutil
import pyperclip
import screen_brightness_control as sbc
import webbrowser
import cv2  # Face Recognition 
import smtplib  # Auto Email Sending
import requests
from bs4 import BeautifulSoup




def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")

    assname = "Jarvis 1.0"
    speak("I am your Assistant")
    speak(assname)


# **Face Recognition Login System**
def face_recognition():
    speak("Scanning face for authentication...")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            speak("Face recognized, access granted!")
            cap.release()
            cv2.destroyAllWindows()
            return True

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("Face not recognized, access denied!")
    return False


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

    elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif "don't listen" in query or "stop listening" in query or "stop ai" in query or "not llistening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

    elif "where is" in query or "my locesion" in query :
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")


    elif "camera" in query or "take a photo" in query or "my photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            speak("camera is on for the taken photo")


    elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
    elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))

    elif "jarvis" in query or "hello ai " in query or "ai" in query:
             
            wishMe()
            speak("yes sir i am herar")
            speak("Jarvis 1 point o in your service Mister")
            speak(assname)     
        
    elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["code"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")

    elif "take screenshot" in command:
        speak("Taking screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved")

    elif "minimize all windows" in command:
        speak("Minimizing all windows")
        keyboard.press_and_release("win + d")

    elif "copy text" in command:
        speak("Copying text")
        pyperclip.copy("This is a copied text")
        speak("Text copied successfully")

    elif "mute volume" in command:
        speak("Muting volume")
        pyautogui.press("volumemute")

    elif "battery status" in command:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"Battery is at {percentage} percent")

    elif "paste text" in command:
        speak("Pasting text")
        keyboard.press_and_release("ctrl + v")

    elif "turn off wifi" in command:
        speak("Turning off WiFi")
        os.system("netsh interface set interface 'Wi-Fi' admin=disable")

    elif "turn on wifi" in command:
        speak("Turning on WiFi")
        os.system("netsh interface set interface 'Wi-Fi' admin=enable")

    elif "turn off bluetooth" in command:
        speak("Turning off Bluetooth")
        os.system("powershell Disable-NetAdapter -Name 'Bluetooth Network Connection' -Confirm:$false")

    elif "turn on bluetooth" in command:
        speak("Turning on Bluetooth")
        os.system("powershell Enable-NetAdapter -Name 'Bluetooth Network Connection' -Confirm:$false")

    elif "next song" in command:
        speak("Skipping to next song")
        keyboard.press_and_release("nexttrack")

    elif "previous song" in command:
        speak("Going to previous song")
        keyboard.press_and_release("prevtrack")

    elif "open excel" in command:
        speak("Opening Microsoft Excel")
        os.system("start excel")

    elif "open powerpoint" in command:
        speak("Opening Microsoft PowerPoint")
        os.system("start powerpnt")

    elif "open vlc player" in command:
        speak("Opening VLC Media Player")
        os.system("start vlc")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "minimize all windows" in command:
        speak("Minimizing all windows")
        keyboard.press_and_release("win + d")

    elif "send whatsapp message" in command:
        speak("Sending WhatsApp message")
        pywhatkit.sendwhatmsg("+919876543210", "Hello, this is a test message", 15, 30)

    
    elif "select all" in command:
        speak("Selecting all text")
        pyautogui.hotkey("ctrl", "a")
    
    elif "open new tab" in command:
        speak("Opening a new tab")
        pyautogui.hotkey("ctrl", "t")

    elif "scroll up" in command:
        speak("Scrolling up")
        pyautogui.scroll(500)

    elif "scroll down" in command:
        speak("Scrolling down")
        pyautogui.scroll(-500)

    elif "press space" in command:
        speak("Pressing space")
        pyautogui.press("space")

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
