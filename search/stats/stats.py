from dataclasses import dataclass
from search.stats.istats import ISearchStats
from timeit import default_timer as timer

@dataclass
class IDAStarStats:
    total_nodes_generated: int = 0
    total_nodes_expanded: int = 0
    ngenerated_iter: int = 0
    nexpanded_iter: int = 0
    tstart: float = 0
    tend: float = 0


    def get_elapsed_time(self) -> float:
        """Returns the elapsed time in seconds."""
        return self.tend - self.tstart 

    def clear_stats(self) -> None:
        """Set to default options the current metrics."""
        self.total_nodes_generated = 0
        self.total_nodes_expanded = 0
        self.ngenerated_iter = 0
        self.nexpanded_iter = 0
        self.tstart = 0
        self.tend = 0

    def start_timer(self) -> None:
        self.tstart = timer()

    def end_timer(self) -> None:
        self.tend = timer()

    def saves_iter(self) -> None:
        """Initialises stats for coming IDA* iteration"""
        self.total_nodes_generated += self.ngenerated_iter
        self.total_nodes_expanded += self.nexpanded_iter
        self.ngenerated_iter = 0
        self.nexpanded_iter = 0

    def add_gnodes(self):
        """Adds # to generated nodes in current iteration."""
        self.ngenerated_iter += 1

    def add_xnodes(self):
        """Adds 1 to expanded nodes in current iteration."""
        self.nexpanded_iter +=1
    
    def show_iter_stats(self, thresh: int | float) -> None:
        print(f"Thresh={thresh} generated: {self.ngenerated_iter:>15} expanded: {self.nexpanded_iter:>15}")
    
    def __str__(self) -> str:
        return f"==============================================================\n" + \
               f"Total nodes generated: {self.total_nodes_generated:>15}\n" + \
               f"Total nodes expaned  : {self.total_nodes_expanded:>15}\n" + \
               f"Elapsed time (sec)   : {self.get_elapsed_time():>15.2f}\n" + \
               f"=============================================================="