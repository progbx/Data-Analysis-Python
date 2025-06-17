"""Template for programming assignment: Generate a Gem Puzzle board"""
import random
from typing import List, Optional


def generate_board(
    size: int = 4,
    tiles: List[Optional[int]] = None
) -> List[List[Optional[int]]]:
    if tiles is None:
        tiles = list(range(1, size * size)) + [None]
        random.shuffle(tiles)
    board = []
    for i in range(size):
        board.append(tiles[i * size:(i + 1) * size])
    return board