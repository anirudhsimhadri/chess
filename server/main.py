from typing import Tuple, List
from socket import socket as Socket

class BadConnection(BaseException): pass
class PasswordMismatch(BaseException): pass

def acceptPlayer(sock: Socket) -> Tuple[Socket, str]:
    conn, addr = sock.accept()

    conn.send(b"chess???")
    ack: bytes = conn.recv(4)
    if ack != b"ack!":
        conn.close()
        raise BadConnection
    
    conn.send(b"user")
    username: str = str(conn.recv(32))
    
    conn.send(b"pass")
    playerPassword: bytes = conn.recv(32)
    if playerPassword != b"password":
        conn.send(b"badpass!")
        conn.close()
        raise PasswordMismatch
    conn.send(b"loggedin")

    return (conn, username)

def serve(port: int):
    sock: Socket = Socket()
    sock.bind(("0.0.0.0", port))
    sock.listen()

    p1Conn: Socket | None = None
    p1Name: str | None = None
    p2Conn: Socket | None = None
    p2Name: str | None = None

    while True:
        try:
            p1Conn, p1Name = acceptPlayer(sock)
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
            p2Conn, p2Name = acceptPlayer(sock)
            break
        except BadConnection:
            print("P2 couldn't connect properly")
            continue
        except PasswordMismatch:
            print("P2's password was incorrect")
            continue
    
    print("P2 connected with name {}".format(p2Name))
