from typing import Literal, Any

class ChessPiece:
    """Common interface for all pieces (DONT INHERIT)"""
    color: Literal["white", "black"]
    MaterialValue: int

    def is_valid_move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        matrix: Any # Just trying to avoid a circular import
    ) -> bool:
        return False