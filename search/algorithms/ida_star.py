from dataclasses import dataclass, field
from search.stats.stats import IDAStarStats
from search.states.states import IState
from typing import ClassVar


@dataclass
class IDAStar:
    thresh: int
    init_state: IState = None
    stats: ClassVar[IDAStarStats] = field(default=IDAStarStats(), init=False)
    

    def solve(self):
        # remove previous stats.
        self.stats.clear_stats()
        # start measuring the elapsed time.
        self.stats.start_timer()
        
        success = False
        while not success:
            # init stats for the current IDA iteration.
            # It also saves stats for previous iterations.
            self.stats.init_iter()

            # search iter
            success = self._solve(self.init_state)

            print(f"T: {self.thresh:2} nodos generados: {self.stats.ngenerated_iter}")
        
            # update thresh.
            # TODO: Abstraer la actualización del thresh del algoritmo.
            self.thresh += 2

        # end measuring the elapsed time.
        self.stats.end_timer()
        # get the elapsed time.
        print(f"Elapsed time to solve: {self.stats.get_elapsed_time():5f} sec.")


    def _solve(self, state: IState) -> bool:

        if state.isgoal():
            #print(f"Solution found")
            return True

        children = state.get_children()
        # añadir stats.
        self.stats.add_xnodes()                 # take into account the expanded node.
        self.stats.add_gnodes(len(children))    # take into account the generated nodes.
        
        for child in children:
            # if h+g <= T keep searching.
            if child.get_h() + child.get_g() <= self.thresh:
                
                if self._solve(child):
                    return True
        
        return False
         