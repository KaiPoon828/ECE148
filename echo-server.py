# echo-server.py
import pyaudio
import pyttsx3
import socket
import time

flag = 0
HOST = "192.168.113.50"  # Standard loopback interface address (localhost)
PORT = 11113  # Port to listen on (non-privileged ports are > 1023)

def terminate():
    global flag
    x = input()
    if x == "end":
        flag = 1

if __name__ == '__main__':
    engine = pyttsx3.init()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    print(data.decode())
                    # engine.say(data.decode())
                    # engine.runAndWait()

                    if not data:
                        break
                    # conn.sendall(data)
                    conn.sendall(('message received: ' + data.decode()).encode())
                    time.sleep(0.1)

                    if data.decode() == 'exit':
                        # Added 
                        pass