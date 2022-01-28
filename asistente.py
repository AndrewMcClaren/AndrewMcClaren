import pyttsx3
import engineio

engineio = pyttsx3.init()
voice = engineio.getProperty("voices")
engineio.setProperty("rate", 130)
engineio.getProperty("voice", voices[0].id)

speak("Hola Pipe que deseas hacer hoy")
