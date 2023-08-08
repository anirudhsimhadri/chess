"""
Two Player Lan Chess
By: Sam Aven, Ani Simhadri, Andrew Voss
This project was created during an intership with PRI Global
Purpose of this file: Handles connection to the server
"""
from socket import socket as Socket

class BadConnection(BaseException): pass
class PasswordMismatch(BaseException): pass

def connectToServer(
    addr: str,
    port: int,
    name: str,
    password: str
) -> Socket:
    sock: Socket = Socket()
    sock.connect((addr, port))

    msg: bytes = sock.recv(8)
    if msg != b"chess???":
        sock.close()
        raise BadConnection
    sock.send(b"ack!")

    msg = sock.recv(4)
    if msg != b"user":
        sock.close()
        raise BadConnection
    sock.send(name.encode())

    msg = sock.recv(4)
    if msg != b"pass":
        sock.close()
        raise BadConnection
    sock.send(password.encode())

    msg = sock.recv(8)
    if msg == b"badpass": raise PasswordMismatch
    elif msg != b"loggedin": raise BadConnection

    return sock
