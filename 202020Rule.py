from time import sleep
from gtts import gTTS
from playsound import playsound
import os
import os.path

assistantRest = 'Assistant Rest.mp3'
assistantResume = 'Assistant Resume.mp3'

def checkAssistant(assistant):

    currentDirectory = os.getcwd() #Dir from where search starts can be replaced with any path

    fileList = os.listdir(currentDirectory)
    
    if assistant in fileList:
        
        return True

    else:

        return False


def saveAssistant(assistant, message):

    if checkAssistant(assistant) is True:

        playsound(assistant)

    else:

        instruction = gTTS(message, lang = 'hi')
        instruction.save(assistant)

        playsound(assistant)

        

def speak(message):

    if 'rest' in message.lower():

        assistant = assistantRest

        saveAssistant(assistant, message)
    

    elif 'resume' in message.lower():

        assistant = assistantResume

        saveAssistant(assistant, message)
    

workTime = 20*60 
restTime = 20 #seconds

while (True):
        
    sleep(workTime)
    
    speak('Asad please take rest for 20 seconds and look 20 feet apart.')

    sleep(restTime)

    speak('Asad your can resume your work now')

