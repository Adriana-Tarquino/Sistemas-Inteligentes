
from queue import PriorityQueue


class Assamble(object):
    
    def __init__(self, cube):
        self.cube = cube
        self.step = None
        
    def manhattan_distance(self):
        distance = 0
        for i in range(6):  
            for j in range(3):  
                for k in range(3):  
                    piece = self.cube.get_cube()[i][j][k]
                    current_position = (i, j, k)
                    goal_position = self.find_piece_position(self.cube.get_goal_cube(), piece)
                    distance += self.calculate_manhattan_distance(current_position, goal_position)
        return distance

    def find_piece_position(self, cube, piece):
        # Buscar la posición de una pieza en el cubo
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if cube[i][j][k] == piece:
                        print(i,j,k)
                        return (i, j, k)
    
    def calculate_manhattan_distance(self, current_position, goal_position):
        # Calcular la distancia de Manhattan entre dos posiciones
        return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1]) + abs(current_position[2] - goal_position[2])
    
    
    def get_possible_moves(self):
        moves = {
            'U': self.cube.U(),
            'U_prime': self.cube.U_prime(),
            'R': self.cube.R(),
            'R_prime': self.cube.R_prime(),
            'L': self.cube.L(),
            'L_prime': self.cube.L_prime(),
            'D': self.cube.D(),
            'D_prime': self.cube.D_prime(),
        }
        return moves

    
    
    
    def solve(self):
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, self.cube.get_cube(), []))  # (total_cost, real_cost, state, moves)
        visited_states = set()
        
        while not priority_queue.empty():
            total_cost, real_cost, current_state, moves = priority_queue.get()
            
            if current_state == self.get_goal_cube():
                return moves
            
            if tuple(current_state) in visited_states:
                continue
            
            visited_states.add(tuple(current_state))
            
            for move_name, move_func in self.get_possible_moves().items():
                new_state = move_func(current_state)
                new_real_cost = real_cost + 1
                new_total_cost = new_real_cost + self.manhattan_distance(new_state)
                new_moves = moves + [move_name]
                priority_queue.put((new_total_cost, new_real_cost, new_state, new_moves))
        
        return None  # No solution found