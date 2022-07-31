import pyttsx3
import os

engine = pyttsx3.init()

engine.say("Good morning kiran")

os.makedirs('Make Working Folder', exist_ok=True)
engine.say("Your woking folder is ready")

engine.runAndWait()
engine.stop()
