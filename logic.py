from actuator import VESC
import time
import speech_recognition as sr
import threading
import socket


class voiceControl:
    def __init__(self, PORT_NAME, IP_ADDRESS, PORT):
        self.motor = VECS(PORT_NAME)
        self.linear_speed = 0.0
        self.steering_angle = 0.0
        self.text_cmd = " "
        self.ip_addr = IP_ADDRESS
        self.port = PORT

        # threading (updating text)
        socket_thread = threading.Thread(target=self._socket_comm())
        socket_thread.start()

        while True:
            self._logic()
            self._execute()


    def _logic(self):
        if self.text == "go":
            self.linear_speed += 0.2
            self.text = " "

        elif self.text == "stop" or self.text == "exit":
            self.linear_speed = 0.0
            self.text = " "

        elif self.text == "left":
            if self.steering_angle <= 0.0:
                self.steering_angle = 0.0
            else:
                self.steering_angle -= 0.1
            self.text = " "

        elif self.text == "right":
            self.steering_angle += 0.1
            self.text = " "

        elif self.text == "straight":
            self.steering_angle = 0.0
            self.text = " "

        elif self.text == "faster":
            self.linear_speed += 0.1
            self.text = " "

        elif self.text == "slower":
            if self.linear_speed <= 0.0:
                self.linear_speed = 0.0
            else:
                self.linear_speed -= 0.1

        else:
            pass


    def _execute(self):
        self.motor.run(self.steering_angle, self.linear_speed)


    def _socket_comm(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip_addr, self.port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by: {addr}")
                    while True:
                        data = conn.recv(1024)
                        self.text = data.decode()

                        if not data:
                            break
                        conn.sendall(('message received: ' + data.decode()).encode())







