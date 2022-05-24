import speech_recognition as sr
import time
import threading
import pyttsx3
flag = 0


def terminate():
    global flag
    x = input()
    if x == "end":
        flag = 1


speech_rec_obj = sr.Recognizer()
count = 0
engine = pyttsx3.init()

while True:
    with sr.Microphone() as source:

        # reduce ambient noise
        if count == 0:
            engine.say("Please be quiet, calibration starts in 3 seconds")
            engine.runAndWait()

            # time.sleep(0.1)
            engine.say("3")
            engine.runAndWait()

            # time.sleep(0.1)
            engine.say("2")
            engine.runAndWait()

            # time.sleep(0.1)
            engine.say("1")
            engine.runAndWait()

            speech_rec_obj.adjust_for_ambient_noise(source, duration=1)
            engine.say("Calibration done.")
            engine.runAndWait()
            count = 1

        engine.say("Speak Anything")
        engine.runAndWait()
        print("speak")
        # terminate_thread = threading.Thread(target=terminate)
        # terminate_thread.start()
        audio = speech_rec_obj.listen(source, phrase_time_limit=1.5)

        try:
            text = speech_rec_obj.recognize_google(audio)
            engine.say(f"You said: {text}")
            engine.runAndWait()

        except:
            engine.say("Sorry could not recognize your voice.")
            engine.runAndWait()
            text = " "

        if text == "end" or text == "end program" or text == "exit" or text == "exit program":
            engine.say("Exiting program")
            engine.runAndWait()
            break
        # time.sleep(0.5)
