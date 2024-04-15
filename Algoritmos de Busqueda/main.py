from StateSpace import *
from Searcher import *
from uniform_cost import *

if __name__ == "__main__":
    debugging = False
    # space_dict = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': [],
    #     'F': []
    # }
    # space_dict = {
    #     '0': ['1', '3'],
    #     '1': ['0', '2', '3', '5'],
    #     '2': ['1', '3', '5', '4'],
    #     '3': ['0', '1', '2', '4'],
    #     '4': ['2', '3', '6'],
    #     '5': ['1', '2'],
    #     '6': ['1', '4'],
    # }
    space_dict = {
        'A': [('B', 4), ('C', 5)],
        'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
        'C': [('A', 5), ('B', 11), ('E', 3)],
        'D': [('B', 9), ('E', 13), ('F', 2)],
        'E': [('B', 7), ('C', 3), ('D', 13), ('F', 6)],
        'F': [('D', 2), ('E', 6)],
    }

    space = StatesSpace()

    state_values = space_dict.keys()
    for state_value in state_values:
        space.add_state(state_value)

    for state_value, state_actions in space_dict.items():
        for action in state_actions:
            space.add_action(state_value, action)

    searcher = Searcher(space, debug=debugging)

    initial_value = 'A'
    goal_value = 'F'
    print("Buscando camino de", initial_value, "a", goal_value, "\n")

    # print("Buscar en profundidad")
    # path = searcher.depth_first(initial_value, goal_value)
    # print(path)

    # space.reset()

    # print("Buscar en amplitud")
    # path = searcher.breadth_first(initial_value, goal_value)
    # print(path)

    space.reset()

    print("Buscar en costo uniforme")
    path, cost = searcher.uniform_cost(initial_value, goal_value)
    print(path, "costo:", cost)