
class State:
    def __init__(self, value):
        self.value = value
        self.actions = []
        self.visited = False
        self.parent = None
        self.cost = None

    def add_action(self, action):
        if not action in self.actions:
            self.actions.append(action)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def was_visited(self):
        return self.visited

    def was_reached(self):
        return self.cost is not None or self.parent is not None
    
    def set_parent(self, value):
        self.parent = value

    def set_cost(self, cost):
        self.cost = cost

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.value} -> {self.actions}"