from dataclasses import dataclass, field
from typing import List
import numpy as np 

AVAILABLE_NPUZZLES = {
    "8": {
        "number_cells": 9,
        "len_board": 3
    },
    
    "15": {
        "number_cells": 16,
        "len_board": 4
    },

    "24": {
        "number_cells": 25,
        "len_board": 5
    }
}

@dataclass(slots=True)
class NPuzzleOperators:
    num: int = 0
    pos: List[int] = field(default_factory=list)


@dataclass
class NPuzzle:
    n: str
    number_cells: int = field(default=0, repr=False)
    len_board: int =field(default=0, repr=False)
    increment_table: np.ndarray = field(default=None, repr=False)
    operators: List[NPuzzleOperators] = field(default_factory=list, repr=False)
    

    def __post_init__(self):
        if self.n not in AVAILABLE_NPUZZLES.keys():
            raise ValueError(f"[ERROR]: {self.n}-puzzle is not available.")
        
        self.number_cells = AVAILABLE_NPUZZLES[self.n]["number_cells"]
        self.len_board = AVAILABLE_NPUZZLES[self.n]["len_board"]
        self.increment_table = np.zeros((self.number_cells, self.number_cells, self.number_cells), dtype=np.int32)
        
        self._init_operators()
        self._init_increment_table()

    def _init_operators(self):
        for blank in range(0, self.number_cells):
            newop = NPuzzleOperators()
            # add a move up
            if blank > self.len_board-1:
                newop.pos.append(blank - self.len_board)
                newop.num +=1
            # add a move left 
            if blank % self.len_board > 0:
                newop.pos.append(blank - 1)
                newop.num +=1
            # add a move right
            if blank % self.len_board < self.len_board-1:
                newop.pos.append(blank + 1)
                newop.num +=1
            # add a move down
            if blank < self.number_cells - self.len_board:
                newop.pos.append(blank + self.len_board)
                newop.num +=1
            self.operators.append(newop)
    
    def _init_increment_table(self):
        for tile in range(1, self.number_cells):
            for source in range(0, self.number_cells):
                for destidx in range(0, self.operators[source].num):
                    dest = self.operators[source].pos[destidx]
                    # round(0.5) -> 0, para evitar esto, round(1+x)-1
                    self.increment_table[tile][source][dest] = round( 1 + (np.abs((tile % self.len_board) - (dest % self.len_board)) - np.abs((tile % self.len_board) - (source % self.len_board)) + np.abs(int(tile / self.len_board) - int(dest / self.len_board)) - np.abs(int(tile / self.len_board) - int(source / self.len_board)) )) - 1


def manhattan(state: np.ndarray) -> int:
    value = 0
    for i in range(len(state)):
        if state[i] != 0:
            value += (np.abs((i%4) - (state[i]%4)) + np.abs(int(i/4) - int(state[i]/4)))
    return value


def get_blank(state: np.ndarray) -> int: 
    for i in range(0, len(state)):
        if state[i] == 0:
            return i
    raise ValueError(f"[ERROR]: The blank did not appear in the state provided.")


    