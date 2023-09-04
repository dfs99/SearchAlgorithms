from typing import Protocol

class ISearchStats(Protocol):

    def get_elapsed_time() -> float:
        ... 

    def clear_stats() -> None:
        ...

    def start_timer() -> None:
        ...

    def end_timer() -> None:
        ...

    def add_gnodes(number_nodes: int) -> None:
        ...

    def add_xnodes(self) -> None:
        ...
        
