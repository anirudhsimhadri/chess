from typing import Tuple
import socket
import random
import net
from chessBoardMatrix import ChessBoardMatrix
from typedef import ChessBoardMatrix as Cbm
from typing import cast
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King

Socket = socket.socket

class BadConnection(BaseException): pass
class PasswordMismatch(BaseException): pass

def runGame(p1: Socket, p2: Socket, p1IsWhite: bool):
    p1Turn = p1IsWhite

    matrix = ChessBoardMatrix(False)

    for col in range(matrix.cols):
        matrix.place_piece(6, col, Pawn("white"))

    for col in range(matrix.cols):
        matrix.place_piece(1, col, Pawn("black"))
    
    matrix.place_piece(0, 0, Rook("black"))
    matrix.place_piece(7, 7, Rook("white"))
    matrix.place_piece(0, 7, Rook("black"))
    matrix.place_piece(7, 0, Rook("white"))

    matrix.place_piece(0, 1, Bishop("black"))
    matrix.place_piece(7, 6, Bishop("white"))
    matrix.place_piece(0, 6, Bishop("black"))
    matrix.place_piece(7, 1, Bishop("white"))
    
    matrix.place_piece(0, 2, Knight('black'))
    matrix.place_piece(7, 5, Knight('white'))
    matrix.place_piece(0, 5, Knight('black'))
    matrix.place_piece(7, 2, Knight('white'))
    
    matrix.place_piece(0, 3, Queen('black'))
    matrix.place_piece(7, 3, Queen('white'))

    matrix.place_piece(0, 4, King('black'))
    matrix.place_piece(7, 4, King('white'))

    game_ended = False

    while not game_ended:
        conn = p1 if p1Turn else p2
        move_start, move_end = net.recvMove(conn)
        print("P1" if p1Turn else "P2", f"moved from {move_start} to {move_end}")
        piece = matrix.chessboard[move_start[0]][move_start[1]]
        target = matrix.chessboard[move_end[0]][move_end[1]]

        print(piece)
        print(target)
        
        if piece is None:
            conn.send(b"no piece")
            continue
        
        was_check = False
        if matrix.is_king_in_check(piece.color):
            was_check = True

        if not piece.is_valid_move(*move_start, *move_end, cast(Cbm, matrix)):
            conn.send(b"invalid!")
            continue

        matrix.move(*move_start, *move_end)

        if matrix.is_king_in_check(piece.color):
            print("king is in check")
            if was_check:
                conn.send(b"check!!!")
            else:
                conn.send(b"pinned!!")
            matrix.undo_move(*move_start, *move_end, target)
            continue

        opp_color = "white" if piece.color == "black" else "black"

        if matrix.is_checkmate(opp_color):
            game_ended = True

        oppConn = p2 if p1Turn else p1
        net.sendMove(oppConn, move_start, move_end)
        if not game_ended:
            conn.send(b"valid!!!")
            oppConn.send(b"yourmove")
        else:
            p1.send(b"gameover")
            p2.send(b"gameover")
        p1Turn = not p1Turn

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

    p1IsWhite = bool(random.getrandbits(1))

    p1Conn.send(b"white!!!" if p1IsWhite else b"black!!!")
    p2Conn.send(b"white!!!" if not p1IsWhite else b"black!!!")

    print("P1 is white" if p1IsWhite else "P2 is white")

    runGame(p1Conn, p2Conn, p1IsWhite)

if __name__ == "__main__": serve(4567, "password")
