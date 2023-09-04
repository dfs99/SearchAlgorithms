import numpy as np 
from search.states.states import FifteenPuzzleState
from search.algorithms.ida_star import IDAStar
from search.domains.npuzzle import manhattan, get_blank


print("Testing IDA*")


instance = np.array(
    [13, 5, 4, 10, 9, 12, 8, 14, 2, 3, 7, 1, 0, 15, 11, 6],
    dtype=np.int32
)


initial_state = FifteenPuzzleState(
    state=instance,
    g=0,
    h=manhattan(instance),
    blank=get_blank(instance),
    oldblank=-1 
)

print(initial_state)

algorithm = IDAStar(manhattan(instance), initial_state)
algorithm.solve()

