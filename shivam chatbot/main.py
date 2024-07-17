import speech_recognition as sr
import webbrowser 
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processComand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://economictimes.indiatimes.com/defaultinterstitial.cms")


if __name__ == "__main__":
    speak("Initializing Shivam....")
    while True:
        # Listen for the wait for Shivam 
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if (word.lower() == "shivam"):
                speak("Ya")
                #listen for the command
                with sr.Microphone() as source:
                    print("Shivam Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processComand(command)

        except Exception as e:
            print("Error; {0}".format(e))
