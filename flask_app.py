#!/usr/bin/env python3                                                                                

import speech_recognition as sr  
import pyttsx3
import ResponseData

from flask import Flask, render_template
from flask import request
import pandas as pd

def matchKeywords(word):
    for x in ResponseData.listResponses:
        for y in x.keywords:
            if (y == word):
                x.count = x.count + 1
    return


#**********************************************************
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/activateKurious')
def activateKurious():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',180)
    engine.setProperty('volume', 0.9) 
    engine.setProperty('voice', voices[1].id)

    keepGoing = True
    error = False
    while keepGoing:
        # get audio from the microphone                                                                       
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            audio = r.listen(source)  

        try:
            #print ("You said " + r.recognize_google(audio))
            sentence = r.recognize_google(audio)
        except sr.UnknownValueError:
            #print("Could not understand audio")
            engine.say("Sorry. I didn't catch that.")
            error = True
            sentence = ""
        except sr.RequestError as e:
            sentence = ""
            engine.say("Sorry. I didn't catch that.")
            error = True
            #print("Could not request results; {0}".format(e))
        
        substrings = ["hello", "hi", "what", "Alexis's", "phone", "number", "email", "address", "contact", "Alexis", "when", "born", "birthday", "When", "you", "your", "name", "purpose", "why", "made", "do", "should", "we", "hire", "give", "job"]

        for x in substrings:
            if(sentence.find(x) != -1): 
                matchKeywords(x)
                
        ResponseData.listResponses.sort(key=lambda x: x.count, reverse=True)

        if(sentence.find("goodbye") != -1):
            keepGoing = False
            engine.say("Goodbye")
        elif(error):
            #error. Don't say anything here.
            error = False
        elif(ResponseData.listResponses[0].count == 0):
            #print("Nothing found")
            engine.say("I'm speechless. I do not know an answer to that question at this time.")
        else:
            engine.say(ResponseData.listResponses[0].response)
        engine.runAndWait()
        
        ResponseData.resetCount(ResponseData.listResponses)
    return render_template("index.html")
    
if __name__ =='__main__':
	app.run(debug=True)
    
    