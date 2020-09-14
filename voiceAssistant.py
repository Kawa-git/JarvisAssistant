from __future__ import print_function
import os
import wolframalpha
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import random
import subprocess

ClinteWolfram = wolframalpha.Client("487PW2-38VPTQHH4R")

def speak(text):
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)

    filename = str(r2) + "randomtext" + str(r1) + ".mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said= r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))

    return said.lower()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")+"-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    notepd = "C:\\Program Files\\Notepad++\\notepad++.exe"
    subprocess.Popen([notepd, file_name])

def opera():
    opera = "D:\\Users\\Ivan\\AppData\\Local\\Programs\\Opera\\launcher.exe"
    subprocess.Popen([opera])

def visual_studio():
    opera = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe"
    subprocess.Popen([opera])


isGoing=True

WAKE ="jarvis"
NOTE_STRS = ["make a note", "write this down", "write this", "remember this", "remember me to", "remember to"]
NAME = ["what's your name", "what is your name", "do you have a name", "have you got a name"]
WOLFRAM = ["search", "research", "what", "what's", "how", "many"]
OPEN_OPERA=["opera","internet"]
OPEN_VISUAL_STUDIO=["open visual studio", "run visual studio", "around visual studio"]
SHUTDOWN = ["quit", "exit", "shut down"]
WEATHER = ["weather", "what's the weather like"]
while isGoing:



    print ("Listening")
    text = get_audio()
    if text.count(WAKE) > 0:
        speak("I am ready")
        text = get_audio()

        for phrase in NOTE_STRS:
            if phrase in text:
                speak("What would you like me to write down?")
                note_text = get_audio()
                note(note_text)
                speak("I've made a note of that.")
        for phrase in NAME:
                if phrase in text:
                    speak("I'm Jarvis, how can i help you?")
        for phrase in SHUTDOWN:
                if phrase in text:
                    speak("Have a nice day")
                    isGoing=False
        for phrase in OPEN_OPERA:
            if phrase in text:
                opera()
                speak("Here we go")

        for phrase in OPEN_VISUAL_STUDIO:
            if phrase in text:
                visual_studio()
                speak("Here we go")

        for phrase in WOLFRAM:
            if phrase in text:
                if text == "what's your name" or  text == "what is your name" or text == "do you have a name":
                    break
                #speak("What should i search?")
                #searchtext = get_audio()
                try:
                    res = ClinteWolfram.query(text)
                    outputWolfram = next(res.results).text
                except:
                    speak("I can't help you, sorry")
                    break
                speak(outputWolfram)
                try:
                    os.remove(filename)
                except:
                    pass
            