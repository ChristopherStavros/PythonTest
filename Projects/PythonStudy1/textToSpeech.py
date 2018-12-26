'''
pip install pyttsx3
python -m pip install pypiwin32

https://rdmilligan.wordpress.com/2015/04/01/text-to-speech-using-python/
'''
import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to Steez-corp corporate headquarters in Hotlanta")
engine.runAndWait() 