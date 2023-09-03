from dataclasses import dataclass
from search.stats.istats import ISearchStats
from timeit import default_timer as timer

@dataclass
class IDAStarStats:
    total_nodes_generated: int = 0
    total_nodes_expanded: int = 0
    ngenerated_iter: int = 0
    nexpanded_iter: int = 0
    tstart: int = 0
    tend: int = 0

    #def get_stats():
    #    pass

    def get_elapsed_time(self):
        return self.tend - self.tstart 

    def clear_stats(self):
        self.total_nodes_generated = 0
        self.total_nodes_expanded = 0
        self.nodes_generated_per_iter = 0
        self.tstart = 0
        self.tend = 0

    def start_timer(self):
        self.tstart = timer()

    def end_timer(self):
        self.tend = timer()

    def init_iter(self):
        self.total_nodes_generated += self.ngenerated_iter
        self.total_nodes_expanded += self.nexpanded_iter
        self.ngenerated_iter = 0
        self.nexpanded_iter = 0

    def add_gnodes(self, number_nodes):
        self.ngenerated_iter += number_nodes

    def add_xnodes(self):
        self.nexpanded_iter +=1