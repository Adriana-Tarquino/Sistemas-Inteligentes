from frontiers import PrioritizedQueue


def uniform_cost(self, intial_value, goal_value):
        return self.weighted_search(intial_value, goal_value, frontier=PrioritizedQueue())