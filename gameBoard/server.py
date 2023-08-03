from typing import Tuple
import socket
import random

Socket = socket.socket

class BadConnection(BaseException): pass
class PasswordMismatch(BaseException): pass

def acceptPlayer(sock: Socket, password: str) -> Tuple[Socket, str]:
    conn, addr = sock.accept()

    conn.send(b"chess???")
    ack: bytes = conn.recv(4)
    if ack != b"ack!":
        conn.close()
        raise BadConnection
    
    conn.send(b"user")
    username: str = conn.recv(32).decode()
    
    conn.send(b"pass")
    playerPassword: str = conn.recv(32).decode()
    if playerPassword != password:
        conn.send(b"badpass!")
        conn.close()
        raise PasswordMismatch
    conn.send(b"loggedin")

    return (conn, username)

def serve(port: int, password: str):
    sock: Socket = Socket()
    sock.bind(("0.0.0.0", port))
    sock.listen()

    print(
        "Serving at address {} on port {}".format(
            socket.gethostbyname(socket.getfqdn()),
            port
        )
    )

    p1Conn: Socket | None = None
    p1Name: str | None = None
    p2Conn: Socket | None = None
    p2Name: str | None = None

    while True:
        try:
            p1Conn, p1Name = acceptPlayer(sock, password)
            break
        except BadConnection:
            print("P1 couldn't connect properly")
            continue
        except PasswordMismatch:
            print("P1's password was incorrect")
            continue

    print("P1 connected with name {}".format(p1Name))

    while True:
        try:
            p2Conn, p2Name = acceptPlayer(sock, password)
            break
        except BadConnection:
            print("P2 couldn't connect properly")
            continue
        except PasswordMismatch:
            print("P2's password was incorrect")
            continue
    
    print("P2 connected with name {}".format(p2Name))

    p1isWhite = bool(random.getrandbits(1))

    p1Conn.send(b"white!!!" if p1isWhite else b"black!!!")
    p2Conn.send(b"white!!!" if not p1isWhite else b"black!!!")

if __name__ == "__main__": serve(4567, "password")
