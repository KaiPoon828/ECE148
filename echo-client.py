import speech_recognition as sr
import time
import threading
import pyttsx3
import socket

HOST = "192.168.113.50"  # The server's hostname or IP address
PORT = 11113  # The port used by the server
flag = 0


def terminate():
    global flag
    x = input()
    if x == "end":
        flag = 1


if __name__ == "__main__":
    text = " "
    speech_rec_obj = sr.Recognizer()
    count = 0
    speech_count = 0
    engine = pyttsx3.init()

    while True:
        with sr.Microphone() as source:

            # reduce ambient noise
            if count == 0:
                engine.say("Please be quiet, calibration starts now")
                engine.runAndWait()

                speech_rec_obj.adjust_for_ambient_noise(source, duration=1)
                engine.say("Calibration done")
                engine.runAndWait()
                count = 1

            # engine.say("Speak Anything")
            # engine.runAndWait()
            print("speak")
            speech_count += 1
            print(f"Number of command: {speech_count}")

            audio = speech_rec_obj.listen(source, phrase_time_limit=1.5)

            try:
                text = speech_rec_obj.recognize_google(audio)
                engine.say(f"You said: {text}")
                engine.runAndWait()

            except:
                engine.say(f"Error 4o4")
                engine.runAndWait()
                text = " "


            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                message = text

                s.sendall(message.encode())
                data = s.recv(1024)

                print(f"Received {data!r}")

            if text == "end" or text == "end program" or text == "exit" or text == "exit program":
                engine.say("Exiting program")
                engine.runAndWait()
                break
            # time.sleep(0.5)