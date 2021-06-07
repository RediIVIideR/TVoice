import eel
import pyttsx3

eel.init('web')


@eel.expose
def tts(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()


@eel.expose
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


eel.start('index.html', size=(800, 800))
