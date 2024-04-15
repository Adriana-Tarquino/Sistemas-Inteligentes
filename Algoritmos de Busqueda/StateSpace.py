
from State import *


class StatesSpace:
    def __init__(self):
        self.space = {}

    def add_state(self, value):
        self.space[value] = State(value)

    def add_action(self, value1, value2):
        self.space[value1].add_action(value2)

    def get_state(self, value):
        if type(value) == tuple:
            return self.space[value[0]]
        else:
            return self.space[value]

    def reset(self):
        self.reset_visited()
        self.reset_costs()

    def reset_costs(self):
        for state in self.space.values():
            state.set_cost(None)

    def reset_visited(self):
        for state in self.space.values():
            state.mark_unvisited()

    def __str__(self):
        return "\n".join(str(state) for state in self.space.values())