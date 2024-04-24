from queue import PriorityQueue
class SearchNode:
    def __init__(self, total_cost, real_cost, state, moves):
        self.total_cost = total_cost
        self.real_cost = real_cost
        self.state = state
        self.moves = moves

    def __lt__(self, other):
        # Definir la comparación para la cola de prioridad
        return self.total_cost < other.total_cost

class Moves(object):
    
    def __init__(self, cube):
       self.cube = cube 
    
    #Rotar una cara del cubo en el sentido de las manecillas del reloj
    def rotate_face_clockwise(self, face): 
        rotated_face = self.cube.get_faces()[face]
        rotated_face = [list(row)[::-1] for row in zip(*rotated_face)]
        self.caras[face] = rotated_face
        
    def rotate_face_counter_clockwise(self, face):
        transposed_face = list(zip(*self.cube.get_faces()[face]))
        print(transposed_face)
        rotated_face = transposed_face[::-1]
        print(rotated_face)
        self.caras[face] = rotated_face
                
        
    def get_faces(self):
        self.cube.show_cube()

    #Rotar una fila en sentido horario
    def U(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][0][i]
            cube[0][0][i] = cube[1][0][i]
            cube[1][0][i] = cube[3][0][i]
            cube[3][0][i] = cube[2][0][i]
            cube[2][0][i] = temp
        
    def U_prime(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][0][i]
            cube[0][0][i] = cube[2][0][i]
            cube[2][0][i] = cube[3][0][i]
            cube[3][0][i] = cube[1][0][i]
            cube[1][0][i] = temp

    #rotar una columana derecha en sentido horario
    def R(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][i][2]  
            cube[0][i][2] = cube[4][i][2]  
            cube[4][i][2] = cube[3][2 - i][2] 
            cube[3][2 - i][2] = cube[5][2 - i][2] 
            cube[5][2 - i][2] = temp 


    def R_prime(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[4][i][2] 
            cube[4][i][2] = cube[0][i][2] 
            cube[0][i][2] = cube[5][2 - i][2]  
            cube[5][2 - i][2] = cube[3][2 - i][2] 
            cube[3][2 - i][2] = temp 

     #rotar una columana a la izquierda en sentido horario
    def L(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][i][0]
            cube[0][i][0] = cube[4][i][0]
            cube[4][i][0] = cube[3][i][0]
            cube[3][i][0] = cube[5][i][0]
            cube[5][i][0] = temp

    def L_prime(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][i][0]
            cube[0][i][0] = cube[5][i][0]
            cube[5][i][0] = cube[3][i][0]
            cube[3][i][0] = cube[4][i][0]
            cube[4][i][0] = temp

    #fila de abajo 
    def D(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][2][i]
            cube[0][2][i] = cube[1][2][i]
            cube[1][2][i] = cube[3][2][i]
            cube[3][2][i] = cube[2][2][i]
            cube[2][2][i] = temp

    def D_prime(self):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[0][2][i]
            cube[0][2][i] = cube[2][2][i]
            cube[2][2][i] = cube[3][2][i]
            cube[3][2][i] = cube[1][2][i]
            cube[1][2][i] = temp


    
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
            'U': self.U,
            'U_prime': self.U_prime,
            'R': self.R,
            'R_prime': self.R_prime,
            'L': self.L,
            'L_prime': self.L_prime,
            'D': self.D,
            'D_prime': self.D_prime,
        }
        return moves

    def solve(self):
        priority_queue = PriorityQueue()
        priority_queue.put(SearchNode(0, 0, self.cube.get_cube(), []))

        visited_states = []
        
        while not priority_queue.empty():
            current_node = priority_queue.get()
            total_cost, real_cost, current_state, moves = current_node.total_cost, current_node.real_cost, current_node.state, current_node.moves
            
            if current_state == self.cube.get_goal_cube():
                return moves
            
            visited_states.append(current_state)
            
            for move_name, move_func in self.get_possible_moves().items():
                new_state = move_func()  # Llama a la función de movimiento sin pasar el estado actual
                if new_state is not None and new_state not in visited_states:
                    new_real_cost = real_cost + 1
                    new_total_cost = new_real_cost + self.manhattan_distance(new_state)
                    new_moves = moves + [(len(moves) + 1, move_name)]  # Formato: (Paso, Movimiento)
                    priority_queue.put(SearchNode(new_total_cost, new_real_cost, new_state, new_moves))
        
            return None

