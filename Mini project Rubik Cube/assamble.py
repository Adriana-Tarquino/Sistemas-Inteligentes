from queue import PriorityQueue
from moves_cube import Moves

class Assamble(object):
    
    def __init__(self, cube, moves):
        self.cube = cube
        self.moves = moves
        
    def manhattan_distance(self, state):
        distance = 0
        goal_cube = self.cube.get_goal_cube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    piece = state[i][j][k]
                    current_position = (i, j, k)
                    goal_position = self.find_piece_position(goal_cube, piece)
                    distance += self.calculate_manhattan_distance(current_position, goal_position)
        return distance

    def find_piece_position(self, cube, piece):
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if cube[i][j][k] == piece:
                        return (i, j, k)
    
    def calculate_manhattan_distance(self, current_position, goal_position):
        return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1]) + abs(current_position[2] - goal_position[2])
    
    def get_possible_moves(self):
        moves = {
            'U': self.moves.U,
            'U_prime': self.moves.U_prime,
            'R': self.moves.R,
            'R_prime': self.moves.R_prime,
            'L': self.moves.L,
            'L_prime': self.moves.L_prime,
            'D': self.moves.D,
            'D_prime': self.moves.D_prime,
        }
        return moves

    def solve(self):
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, self.cube.get_cube(), []))  # (total_cost, real_cost, state, moves)
        visited_states = []
        
        while not priority_queue.empty():
            total_cost, real_cost, current_state, moves = priority_queue.get()
            
            if current_state == self.cube.get_goal_cube():
                return moves
            
            visited_states.append(current_state)
            
            for move_name, move_func in self.get_possible_moves().items():
                new_state = move_func(current_state)
                new_real_cost = real_cost + 1
                new_total_cost = new_real_cost + self.manhattan_distance(new_state)
                new_moves = moves + [(len(moves) + 1, move_name)]  # Formato: (Paso, Movimiento)
                priority_queue.put((new_total_cost, new_real_cost, new_state, new_moves))
        
        return None

