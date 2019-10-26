#!/usr/bin/env python
# coding: utf-8

import socket

HOSTNAME = '127.0.0.1'
PORT = 1337

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOSTNAME, PORT))
    s.listen(1)

    try:
        while True:
            conn, addr = s.accept()
            addr_str = addr[0] + ':' + str(addr[1])
            print('accept client: ' + addr_str)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data + '\n')
            print('disconnect client: ' + addr_str)
            conn.close()
    finally:
        s.close()

if __name__ == "__main__":
    try:
        print('Server running at http://' + HOSTNAME + ':' + str(PORT) + '/');
        listen()
    except KeyboardInterrupt:
        pass
