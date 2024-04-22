#'center': 6,  # 1 centro por cara, 6 caras en total
# 'edge': 12,   # 4 aristas por cara, 6 caras en total
# 'corner': 8    # 4 esquinas por cara, 6 caras en total
    
class RubiksCube:
    def __init__(self, cube):
        self.cube = cube    
        self.caras = {}
        self.intersections = []
        self.corner
               
    def count_caras(self):
        return len(self.cube)
    
    def get_cube(self):
        return self.cube

    

    def assemble(self):
        self.caras['front'] = self.cube[0]
        self.caras['right'] = self.cube[1]
        self.caras['left'] = self.cube[2]
        self.caras['back'] = self.cube[3]
        self.caras['down'] = self.cube[5]
        self.caras['up'] = self.cube[4]
    
    def show_cube_with_caras(self):
        print("Current state of the cube:")
        for face, content in self.caras.items():
            print(face)
            for row in content:
                print(' '.join(row))
            print()  # Separador entre caras
    
    def show_faces(self):
        print("Current state of the cube:")
        for face, content in self.caras.items():
            print(face)
            for row in content:
                print(' '.join(row))
            print()  # Separador entre caras

    # def intersections_cornes(self):
    #     #las esquinas tienen 3 colores:
        
        
        
        
    def intersections_edge(self):
        for cara in self.cube:
            for row in cara[0]:
                print(row)
            print()  

    def show_cube(self):
        for cara in self.cube:
            for row in cara:
                print(' '.join(row))
            print()  # Separador entre caras    
            
    def show_face(self, face):
        for row in self.caras[face]:
            print(' '.join(row))
        
    def rotate_face_clockwise(self, face): #Rotar una cara del cubo en el sentido de las manecillas del reloj
        rotated_face = self.caras[face]
        rotated_face = [list(row)[::-1] for row in zip(*rotated_face)]
        self.caras[face] = rotated_face
        
    def rotate_face_counter_clockwise(self, face):
        transposed_face = list(zip(*self.caras[face]))
        print(transposed_face)
        rotated_face = transposed_face[::-1]
        print(rotated_face)
        self.caras[face] = rotated_face
        
    
    # def U(self):
    #         first_rows = []
    #         # Cambiar el orden de las caras antes de iterar sobre ellas
    #         ordered_faces = ['front', 'up', 'back', 'down', 'left', 'right']
    #         for face in ordered_faces:
    #             first_rows.append(self.caras[face][0])
    #         return first_rows
            
   