import pyttsx3

engine = pyttsx3.init()

name = input("Enter your name : ")
sys_say = f"Hello {name}"

engine.say(sys_say)
engine.runAndWait()
engine.stop()

input()