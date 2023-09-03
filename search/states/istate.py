from typing import Protocol
from typing import List, Any


class IState(Protocol):
    """TODO: Actualmente es de búsqueda informada. revisar"""

    def get_g() -> int:
        """Returns the actual cost from the initial state"""
    
    def get_h() -> int:
        """Returns the heuristic cost from the current state."""

    def isgoal() -> bool:
        """"""

    def get_children() -> List:
        """Returns a list of successors."""