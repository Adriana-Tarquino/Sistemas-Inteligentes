from frontiers import Queue


def breadth_first(self, intial_value, goal_value):
        return self.search(intial_value, goal_value, frontier=Queue())