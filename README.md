AI Assistant
Overview
 AI-powered personal assistant built using Python. It integrates speech recognition, text-to-speech, face recognition, and various system and application controls to help users perform tasks hands-free. The assistant can execute commands like controlling the system's volume, brightness, opening applications, and even send WhatsApp messages. It can also search the web, take notes, take screenshots, and much more!

Features
Voice Command Support: The assistant listens to your voice commands and responds with actions.

Face Recognition Login: Using your webcam, Jarvis can recognize your face and provide system access.

System Controls: Control system brightness, volume, and even lock or shut down your PC with voice commands.

Multimedia: Play videos on YouTube, take screenshots, and control media playback.

Weather Info: Get current weather details based on your location.

File Management: Write and show notes, perform copy-paste actions, and open/close applications.

WhatsApp Messaging: Send WhatsApp messages directly from the assistant.

Prerequisites
Python 3.x installed.

The following libraries need to be installed:

pyttsx3

speech_recognition

pyautogui

webbrowser

os

pywhatkit

keyboard

psutil

pyperclip

screen_brightness_control

opencv-python

smtplib

requests

beautifulsoup4

You can install the required libraries using the following commands:

bash
Copy
pip install pyttsx3 speech_recognition pyautogui pywhatkit keyboard psutil pyperclip opencv-python requests beautifulsoup4
How to Run
Clone or download this repository to your local machine.

Ensure all the dependencies are installed (refer to the prerequisites section).

Open a terminal and navigate to the directory where the script is located.

Run the script using:

bash
Copy
python jarvis_assistant.py
The assistant will greet you and start listening for commands.

Command List
Voice Control Commands:

search on google <query>: Searches the web on Google.

search on youtube <query>: Plays a video on YouTube.

play <query>: Plays a song/video on YouTube.

brightness up: Increases screen brightness.

brightness down: Decreases screen brightness.

volume up: Increases system volume.

volume down: Decreases system volume.

pause video: Pauses a video.

play video: Plays a paused video.

shutdown: Shuts down the computer.

restart: Restarts the computer.

lock: Locks the computer screen.

weather: Fetches the weather for your location.

take a photo: Takes a photo using the webcam.

write a note: Writes a note to a text file.

show note: Displays saved notes.

send whatsapp message: Sends a WhatsApp message.

take screenshot: Takes a screenshot of the screen.

minimize all windows: Minimizes all open windows.

battery status: Shows battery percentage.

turn off wifi: Turns off Wi-Fi.

turn on wifi: Turns on Wi-Fi.

turn off bluetooth: Turns off Bluetooth.

turn on bluetooth: Turns on Bluetooth.

Face Recognition Login:

The assistant will prompt you to authenticate using your face before granting access.

File Management:

select all: Selects all text on the screen.

copy text: Copies a predefined text to clipboard.

paste text: Pastes text from the clipboard.

Configuration
API Key for Weather: To get weather information, you need an API key from OpenWeatherMap. Replace the placeholder "Api key" with your actual API key in the weather command section.

Troubleshooting
Face Recognition Not Working:

Make sure you have a functional webcam.

Ensure that the opencv-python package is installed properly.

Voice Command Not Recognized:

Ensure the microphone is set up correctly.

You may need to adjust the microphone's sensitivity settings in your operating system.

Dependencies Missing:

If any required libraries are not installed, use the following command to install them:

bash
Copy
pip install <library_name>
