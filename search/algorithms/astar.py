from dataclasses import dataclass, field
from search.states.states import IState
from heapq import heappush, heappop
from typing import Any, List, Set

@dataclass
class AStar:
    init_state: IState
    open: List[IState] = field(default_factory=list, init=False, repr=False)
    closed: Set[int] = field(default_factory=set, init=False, repr=False)
    stats: Any = field(default=None, init=False, repr=False)

    def __post_init__(self):
        # add to open the initial state.
        heappush(self.open, self.init_state)
        

    def solve(self):
        generated = 0
        expanded = 0
        from timeit import default_timer as timer
        start = timer()
        while (len(self.open) > 0):
            
            # get from open the first node with lower f-value.
            current_state: IState = heappop(self.open)

            # if the current node already expanded, continue.
            if current_state.__hash__() in self.closed:
                continue
            
            # if goal found, exit.
            if current_state.isgoal():
                print(f"solution found!")
                break 
            
            # add current to closed.
            self.closed.add(current_state.__hash__())
            expanded+=1
            # expand current state and store its children to open list.
            for child in current_state.get_children():
                generated+=1
                heappush(self.open, child)

        print(f"Elapsed time: {timer()-start}")
        print(f"generated nodes: {generated}")
        print(f"expanded nodes: {expanded}")
        print(current_state)
        return
        #raise NotImplementedError("To be implemented.s")