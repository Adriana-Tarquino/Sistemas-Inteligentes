from frontiers import Stack


def depth_first(self, intial_value, goal_value):
        return self.search(intial_value, goal_value, frontier=Stack())
