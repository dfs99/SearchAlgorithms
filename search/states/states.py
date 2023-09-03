from dataclasses import dataclass, field
from typing import ClassVar, List
from search.states.istate import IState
from search.domains.fifteenpuzzle import FifteenPuzzle
import numpy as np


@dataclass(slots=True, frozen=True, unsafe_hash=True)
class FifteenPuzzleState:
    domain: ClassVar[FifteenPuzzle] = field(default=FifteenPuzzle(), init=False, repr=False) 
    g: int
    h: int
    state: np.ndarray
    blank: int
    oldblank: int

    def get_g(self) -> int:
        return self.g 
    
    def get_h(self) -> int:
        return self.h
    
    def isgoal(self) -> bool:
        # For the 15puzzle it's enough to check that its h-value has reached 0.
        return self.get_h() == 0

    def get_children(self) -> List:

        successors: List[FifteenPuzzleState] = []
        
        for index in range(0, FifteenPuzzleState.domain.operators[self.blank].num):
            newblank = FifteenPuzzleState.domain.operators[self.blank].pos[index]
            if newblank != self.oldblank:   # avoid to generate the father's node.
                tile = self.state[newblank]
                new_state = self.state.copy()   # make a copy.
                new_state[self.blank] = tile
                new_state[newblank] = 0
                successors.append(
                    FifteenPuzzleState(
                        g=self.get_g() + 1,
                        h=self.get_h() + FifteenPuzzleState.domain.increment_table[tile][newblank][self.blank],
                        state=new_state,
                        blank=newblank,
                        oldblank=self.blank
                    )
                )
        return successors
