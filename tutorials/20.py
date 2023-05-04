# networking

import socket
import sys

s = socket.socket()
print('socket created')
port = 40674

if sys.argv[1] == 'server':
    s.bind(('', port))
    print(f'socket bound to {port}')
    s.listen()
    print('socket is listening...')

    while True:
        c, addr = s.accept()
        print('got message from', addr)
        c.send(b'Thanks for connecting!')
        c.close()
elif sys.argv[1] == 'client':
    s.connect(('127.0.0.1', port))
    print(s.recv(1024))
    s.close()
