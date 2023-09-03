from typing import Protocol

class IAlgorithm(Protocol):
    
    def solve() -> None:
        ...