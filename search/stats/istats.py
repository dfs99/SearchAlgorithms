from typing import Protocol

class ISearchStats(Protocol):

    def get_elapsed_time(self):
        ... 

    def clear_stats(self):
        ...

    def start_timer(self):
        ...

    def end_timer(self):
        ...

    def init_iter(self):
        ...

    def add_gnodes(self, number_nodes):
        ...

    def add_xnodes(self):
        ...
        