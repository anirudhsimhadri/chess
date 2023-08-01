"""
This module contains interfaces for commonly used types.
These interfaces can be used in place of the actual types in type hints,
Preventing circular imports
"""
from typing import Literal, TypeVar

T = TypeVar("T")
def unwrap(opt: T | None) -> T:
    """Convert a `T|None` into a `T`, asserting that it isn't `None`"""
    assert opt is not None
    return opt

class ChessBoardMatrix:
    """
    Interface for the matrix to avoid circular imports
    This interface is implemented in chessBoardMatrix.py
    """
    rows: Literal[8]
    cols: Literal[8]
    chessBoard: list[list["ChessPiece"]]

class ChessPiece:
    """Common interface for all pieces (DONT INHERIT)"""
    color: Literal["white", "black"]
    pieceType: str
    MaterialValue: int

    def is_valid_move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        matrix: ChessBoardMatrix
    ) -> bool:
        return False
    
    def all_valid_moves(
        self,
        start_row: int,
        start_col: int
    ) -> list[tuple[int, int]]:
        return []