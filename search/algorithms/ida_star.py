from dataclasses import dataclass, field
from search.stats.stats import IDAStarStats
from search.states.states import IState
from typing import ClassVar

NEXT_THRESH_VALUE = 9999

@dataclass
class IDAStar:
    thresh: int | float
    next_thresh: int | float = field(default=NEXT_THRESH_VALUE, init=False)    # used to store the min value that exceeds the current T. 
    init_state: IState
    stats: ClassVar[IDAStarStats] = field(default=IDAStarStats(), init=False)

    def update_threshold(self):
        self.thresh = self.next_thresh
        self.next_thresh = NEXT_THRESH_VALUE

    def solve(self):
        # try to remove previous stats if exists.
        self.stats.clear_stats()
        # start measuring the elapsed time.
        self.stats.start_timer()
        
        success = False
        while not success:

            # search iter
            success = self._solve(self.init_state)

            # print stats for the current iteration.
            self.stats.show_iter_stats(self.thresh)
            
            # update thresh.
            self.update_threshold()

            # init stats for the following IDA iteration.
            # It also saves stats for current iterations.
            self.stats.saves_iter()

        # end measuring the elapsed time.
        self.stats.end_timer()
        
        # print stats
        print(self.stats)
        

    def _solve(self, state: IState) -> bool:

        if state.isgoal():
            return True

        children = state.get_children()
        # añadir stats.
        self.stats.add_xnodes()                 # take into account the expanded node.
        self.stats.add_gnodes(len(children))    # take into account the generated nodes.
        
        for child in children:
            # if h+g <= T keep searching.
            f_value = child.get_h() + child.get_g()
            if  f_value <= self.thresh:
                if self._solve(child):
                    return True
            # else, update thresh.
            else:
                self.next_thresh = f_value if f_value < self.next_thresh else self.next_thresh 
        
        return False
         