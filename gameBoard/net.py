"""
Two Player Lan Chess
By: Sam Aven, Ani Simhadri, Andrew Voss
This project was created during an intership with PRI Global
Purpose of this file: Sends move to and from client
"""
"""
Sending moves between server and client

Moves are sent in a uniform fixed-length format (always 4 bytes):
Starting row (1 byte, '1'..'8' ascii)
Starting col (1 byte, 'a'..'h' ascii)
Ending row (1 byte, '1'..'8' ascii)
Ending col (1 byte, 'a'..'h' ascii)

Neither side of the connection should ever send or receive 2 moves back to back
A typical connection should look like:
Player 1 sends a move to the server
Server responds to player 1 and sends the move to player 2 if it is valid
Player 2 sends a move to the server
Server responds to player 2 and sends the move to player 1 if it is valid
...

The functions provided by this module should be used by both the client and server to send and receive moves
"""

from typing import Tuple
from socket import socket as Socket

def serializeCoord(coord: Tuple[int, int]) -> bytes:
    row, col = coord

    return bytes([ord(b'1') + row]) + bytes([ord(b'a') + col])

def deserializeCoord(ser: bytes) -> Tuple[int, int]:
    row = ser[0] - ord(b'1')
    col = ser[1] - ord(b'a')

    return row, col

def sendMove(conn: Socket, start_pos: Tuple[int, int], end_pos: Tuple[int, int]):
    conn.send(serializeCoord(start_pos) + serializeCoord(end_pos))

def recvMove(conn: Socket) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    ser = conn.recv(4)

    start_pos = deserializeCoord(ser[:2])
    end_pos = deserializeCoord(ser[2:])

    return start_pos, end_pos
