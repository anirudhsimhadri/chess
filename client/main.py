from socket import socket as Socket

class BadConnection(BaseException): pass

def connectToServer(port: int, name: str, password: str) -> Socket:
    sock: Socket = Socket()
    sock.connect(("localhost", port))

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

    return sock