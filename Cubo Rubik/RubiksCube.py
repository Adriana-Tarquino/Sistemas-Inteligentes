
class Validator(object):
    #'center': 6,  # 1 centro por cara, 6 caras en total
    # 'edge': 12,   # 4 aristas por cara, 6 caras en total
    # 'corner': 8    # 4 esquinas por cara, 6 caras en total
    def __init__(self, cube):
        self.cube = cube
        
    def validate_center(self):
        centers = set()
        for face in self.cube.get_cube():
            center_color = face[1][1]
            if center_color in centers:
                print("Error: Duplicated center:", center_color)
            centers.add(center_color)
    
    def validate_adjacents(self):
        #cara, row, center
        cube = self.cube.get_cube()
        for i in range(len(cube)-1):
            if cube[i][1][1] == cube[i + 1][1][1]:
                print("Error: Invalid Center in face", cube[i][1][1])        
        
       
    def validate_cara(self):
        if self.cube.count_caras() != 6:
            print("Error: Invalid missing rubik's cube face")
            
    def validate_color(self):
        for cara in self.cube.get_cube():
            for row in cara:
                if len(row) != 3:
                    print("Error: invalid missing color", row)

    def validate_dimensions(self):
        shape = (len(self.cube.get_cube()), len(self.cube.get_cube()[0]), len(self.cube.get_cube()[0][0]))
        # print("Dimensions of cube:", shape)   
        if shape != (6, 3, 3):
          print("Error: Dimensions of cube")
   

# class Move(object):
#     def 


class RubiksCube:
    def __init__(self, cube):
        self.cube = cube    
        self.caras = {}
               
    def count_caras(self):
        return len(self.cube)
    
    def get_cube(self):
        return self.cube
    
    # def pieces(self):

    def assemble(self):
        self.caras['front'] = self.cube[0]
        self.caras['right'] = self.cube[1]
        self.caras['left'] = self.cube[2]
        self.caras['down'] = self.cube[3]
        self.caras['up'] = self.cube[4]
        self.caras['back'] = self.cube[5]
    
    def show_cube_with_caras(self):
        print("Current state of the cube:")
        for face, content in self.caras.items():
            print(face)
            for row in content:
                print(' '.join(row))
            print()  # Separador entre caras
    
    
    def show_cube(self):
        for cara in self.cube:
            for row in cara:
                print(' '.join(row))
            print()  # Separador entre caras    
        
    def rotate_face_clockwise(self, face): #Rotar una cara del cubo en el sentido de las manecillas del reloj
        rotated_face = self.caras[face]
        rotated_face = [list(row)[::-1] for row in zip(*rotated_face)]
        self.caras[face] = rotated_face
