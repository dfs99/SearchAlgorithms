from typing import Protocol


class IDomain(Protocol):

    def operators() -> None:
        ... 