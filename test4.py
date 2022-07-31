import pyttsx3
import os

engine = pyttsx3.init()

engine.say("Good morning kiran")

os.makedirs('Make Working New Folder', exist_ok=True)
engine.say("Your woking new folder is ready")

engine.runAndWait()
engine.stop()
