import speech_recognition as sr
import time
import threading

flag = 0


def terminate():
    global flag
    x = input()
    if x == "end":
        flag = 1


speech_rec_obj = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Speak anything ")
        terminate_thread = threading.Thread(target=terminate)
        terminate_thread.start()

        speech_rec_obj.adjust_for_ambient_noise(source, duration=0.2)
        audio = speech_rec_obj.listen(source, phrase_time_limit=1)

        try:
            text = speech_rec_obj.recognize_google(audio)
            print(f"You said: {text}")

        except:
            print("Sorry could not recognize your voice.")

        if flag == 1:
            print("End speech recognition.")
            break
        time.sleep(0.5)
