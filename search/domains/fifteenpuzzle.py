from dataclasses import dataclass, field
from typing import List
import numpy as np 


@dataclass(slots=True)
class NPuzzleOperators:
    num: int = 0
    pos: List[int] = field(default_factory=list)


@dataclass
class FifteenPuzzle:
    number_cells: int = 16
    len_board: int = 4
    operators: List[NPuzzleOperators] = field(default_factory=list, repr=False)
    increment_table: np.ndarray = field(default_factory=lambda : np.zeros((16, 16, 16), dtype=np.int32), repr=False)
    terminal_state: List[int] = field(default_factory=lambda : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #initial_state: List[int] = field(default_factory=list)

    def __post_init__(self):
        self._init_operators()
        self._init_increment_table()

    #def fetch_state(self):
        # todo: hacer que se lea desde std in.
    #    self.initial_state = [14, 13, 15, 7, 11, 12, 9, 5, 6, 0, 2, 1, 4, 8, 10, 3] 

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


if __name__ == "__main__":
    print("testing...")
    domain = FifteenPuzzle()
    domain.fetch_state()
    print(domain)

    