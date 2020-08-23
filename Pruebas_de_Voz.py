# -*- coding: utf-8 -*-
"""
Pruebas de voz para saber que es lo que capta el micrófono.

@author: Magh
"""

import speech_recognition as sr

r = sr.Recognizer() 

with sr.Microphone() as source:
    print('Por favor, hable. ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Tu dijiste: {}'.format(text))
    except:
        print('No te escuché xD')