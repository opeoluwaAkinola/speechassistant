import random

import speech_recognition as sr
import webbrowser
from time import strftime
import time
from datetime import date
import playsound
from gtts import gTTS
import os
r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            houseboy_speek(ask)
        audio=r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            houseboy_speek('Sorry, I did not get that')
            return None
        except sr.RequestError:
            houseboy_speek('Sorry my speech service is down')
            return None
        return voice_data
def houseboy_speek(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    # r = random.randint(1,1000000)
    audio_file = 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        houseboy_speek('my name is Houseboy')
    if 'what time is it?' in voice_data or 'what is the time' in voice_data:
        houseboy_speek(strftime('%H:%M'))
    if "what is today's date" in voice_data:
        houseboy_speek(date.today())
    if 'search' in voice_data:
        search=record_audio('what do you want to search for')
        url=f'https://google.com/search?q={search}'
        webbrowser.get().open(url)
        houseboy_speek('Here is what i found')
    if 'find location' in voice_data:
        location=record_audio('what is the location')
        url=f'https://google.nl/maps/place/{location}/&amp;'
        webbrowser.get().open(url)
        houseboy_speek('Here is the location of '+location)
    if exit in voice_data:
        exit()
time.sleep(1)
houseboy_speek('how can i help you')
while 1:
    if record_audio():
        voice_data=record_audio()
        respond(voice_data)