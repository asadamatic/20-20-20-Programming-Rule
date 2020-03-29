from time import sleep
from gtts import gTTS
from playsound import playsound
import os
import os.path

assistant = 'Assistant.mp3'


def checkAssistant(assistant):

    currentDirectory = os.getcwd() #Dir from where search starts can be replaced with any path

    fileList = os.listdir(currentDirectory)
    
    if assistant in fileList:
        
        return True

    else:

        return False

def speak(message):

    if checkAssistant(assistant) is True:

        pass

    else:

        instruction = gTTS(message, lang = 'hi')
        instruction.save(assistant)

    playsound(assistant)
        


workTime = 20*60 
restTime = 20 #seconds

while (True):
        
    for time in range(workTime):

        sleep(1)
        

    for time in range(restTime):

        sleep(1)
    
    
    speak('Asad please take rest for 20 seconds and look 20 feet apart.')


