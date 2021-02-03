import speech_recognition as sr
import webbrowser 
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer() 

def record_audio(ask = False):
  with sr.Microphone() as source:
    if ask:
      sierra_speak(ask)
    audio = r.listen(source)
    voice_data = ''
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      sierra_speak('sorry I did not get that')
    except sr.RequestError:
      sierra_speak('sorry my speech service is down')
    return voice_data

def sierra_speak(audio_string):
  tts = gTTS(text=audio_string, lang='en')
  r = random.randint(1, 10000000)
  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

def respond(voice_data):
  if 'what is your name' in voice_data:
    sierra_speak('my name is sierra')
  if 'what time is it' in voice_data:
    sierra_speak(ctime())
  if 'search' in voice_data:
    search = record_audio('what would you like to search for?')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    sierra_speak('here is what i found for ' + search)
  if 'find location' in voice_data:
    location = record_audio('where would you like to find?')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    sierra_speak('here is what i found for the location ' + location)
  if 'exit' in voice_data:
    exit()

time.sleep(1)
sierra_speak('how can I help you?')  
while 1:
  voice_data = record_audio()
  respond(voice_data)