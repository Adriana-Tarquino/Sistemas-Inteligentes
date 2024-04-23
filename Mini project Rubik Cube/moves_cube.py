from rubiks_cube import RubiksCube

class Moves(object):
    
    def __init__(self, cube):
        self.cube = cube
    
    def rotate_face_clockwise(self, face): #Rotar una cara del cubo en el sentido de las manecillas del reloj
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
    def U(self, pos):
        cube = self.cube.get_cube()
        for i in range(3):
            temp = cube[pos][0][i]
            cube[pos][0][i] = cube[pos + 1][0][i]
            cube[pos + 1][0][i] = cube[pos + 3][0][i]
            cube[pos + 3][0][i] = cube[pos +2][0][i]
            cube[pos + 2][0][i] = temp

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
            print(temp)
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

