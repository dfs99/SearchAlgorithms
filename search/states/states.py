from dataclasses import dataclass, field
from typing import ClassVar, Generator, Any
from search.states.istate import IState
from search.domains.npuzzle import NPuzzle
import numpy as np


@dataclass(slots=True, frozen=True, unsafe_hash=True)
class FifteenPuzzleState:
    domain: ClassVar[NPuzzle] = field(default=NPuzzle("15"), init=False, repr=False) 
    state: np.ndarray
    g: int
    h: int 
    blank: int 
    oldblank: int 

    def get_g(self) -> int:
        return self.g 
    
    def get_h(self) -> int:
        return self.h
    
    def isgoal(self) -> bool:
        # For the 15puzzle it's enough to check that its h-value has reached 0.
        return self.get_h() == 0

    def get_children(self) -> Generator["FifteenPuzzleState", Any, None]:
        """A generator function is used to generate on demand children."""
        
        for index in range(0, FifteenPuzzleState.domain.operators[self.blank].num):
            newblank = FifteenPuzzleState.domain.operators[self.blank].pos[index]
            if newblank != self.oldblank:   # avoid to generate the father's node.
                tile = self.state[newblank]
                new_state = self.state.copy()   # make a copy.
                new_state[self.blank] = tile
                new_state[newblank] = 0
                yield FifteenPuzzleState(
                        state=new_state,
                        g=self.get_g() + 1,
                        h=self.get_h() + FifteenPuzzleState.domain.increment_table[tile][newblank][self.blank],
                        blank=newblank,
                        oldblank=self.blank
                    )


    def __str__(self):
        msg = "=================\n"
        msg += " 15-Puzzle State\n"
        msg += "-----------------\n"
        for i in range(0, len(self.state)):
            msg += f" {self.state[i]:2}"
            if (i+1)%4 == 0:
                msg += f" \n"
        msg += "-----------------\n"
        msg += f"\n g cost : {self.g:>5}\n" + \
               f" h value: {self.h:>5}\n" + \
            "=================\n"
        return msg