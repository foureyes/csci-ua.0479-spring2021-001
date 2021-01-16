import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '', 5000
queue = 5
s.bind((host, port))
s.listen(queue)
while True:
    # fill in the code to implement your talk_to_me_server.py
    pass

