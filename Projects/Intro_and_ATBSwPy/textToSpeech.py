'''
pip install pyttsx3
python -m pip install pypiwin32

https://rdmilligan.wordpress.com/2015/04/01/text-to-speech-using-python/
'''
import pyttsx3
engine = pyttsx3.init()
#text = "Welcome to Steez-corp corporate headquarters in Hotlanta"
text_input = input()

def speak(text):
    engine.say(text)
    engine.runAndWait() 

speak(text_input)