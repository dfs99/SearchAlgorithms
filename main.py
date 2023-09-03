import numpy as np 
from search.states.states import FifteenPuzzleState
from search.algorithms.ida_star import IDAStar

print("Probando el IDA*")
print("Primera instancia de korf: ")
i1 = [14, 13, 15, 7, 11, 12, 9, 5, 6, 0, 2, 1, 4, 8, 10, 3]
i2 = [13, 5, 4, 10, 9, 12, 8, 14, 2, 3, 7, 1, 0, 15, 11, 6]
i1 = i2
def manhattan(state) -> int:
    value = 0
    for i in range(len(state)):
        if state[i] != 0:
            value += (np.abs((i%4) - (state[i]%4)) + np.abs(int(i/4) - int(state[i]/4)))
    return value


def get_blank(state) -> int:
    for i in range(0, len(state)):
        if state[i] == 0:
            return i
print(f"h valor: {manhattan(i1)}")


s1 = FifteenPuzzleState(0, manhattan(i1), np.array(i1, dtype=np.int32), get_blank(i1), -1)

print(s1)

algorithm = IDAStar(manhattan(i1), s1)
print(algorithm)

algorithm.solve()

