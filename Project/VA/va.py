import os
import time
import webbrowser
import uuid
import re
import playsound
from gtts import gTTS
import speech_recognition as sr
'''
text ="Welcome to Codegnan,hope you are doing well"
#convert above text to speed
tts=gTTS(text)
#print(tts)
tts.save("audio.mp3")
playsound.playsound("audio.mp3")
'''

#we will use Speechrecognition
#we will create a listen function to listen

def listen():
    """function to listen the voice"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("start taking clearly")
        audio = r.listen(source,phrase_time_limit=10)
    data = "" #this will be your statement
    #exception handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear your voice")
    except sr.RequestError as e:
        print("Request failed")
    return data
    #tts=gTTS(data,lang = "fr",tld="fr")
    #tts.save("Speech.mp3")
    #playsound.playsound("Speech.mp3")
#listen()


#now we will create a function to respond back


def respond(String):
    """Respond Function"""
    print(String)
    tts=gTTS(String)
    tts.save('Speech.mp3')
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    

#now we will create our assistant function to make conversation

def va(data):
    """VirtualAssistant Actions"""
    if "how are you" in data:
        listening=True
        respond("I am doing good,hope you are fine")
    elif"what are your plans" in data:
        listening =True
        respond("Today you have weekend exam")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "open google" in data.casefold():
        listen = True
        reg_ex=re.search("open google(.*)",data)
        url= "https://www.google.com/"
        if reg_ex:
            sub = erg_ex.group(1)
            url = url + 'r/'
            print(url)
        webbrowser.open(url)
        respond("Successfully done")
    elif "locate" in data.casefold():
        listening = True
        webbrowser.open("https://www.google.com/maps/@17.5042511,78.3955875,15z?entry=ttu&g_ep=EgoyMDI2MDgyNi4wIKXMDSoASAFQAw%3D%3D/search/" +data.replace("locate",""))
        respond ("located")
    elif"stop talking" in data:
        listening = False
        respond("Okay cool......kopadaku take care..")
    try:
        return listening
    except UnboundLocalError:
        print("Time out")
respond("Hey jyothi...Good Day,how are you")
#greeting from assistant
listening = True
while listening:
    data = listen()
    listening =va(data)
    


    
