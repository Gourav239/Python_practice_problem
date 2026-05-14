# Install an external module and use it to perform an operation of your interest 

import pyfiglet
import pyttsx3


text = pyfiglet.figlet_format("Gourav")
print(text)

engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()