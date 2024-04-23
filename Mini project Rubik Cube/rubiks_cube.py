#'center': 6,  # 1 centro por cara, 6 caras en total
# 'edge': 12,   # 4 aristas por cara, 6 caras en total
# 'corner': 8    # 4 esquinas por cara, 6 caras en total
    
class RubiksCube:
    def __init__(self, cube):
        self.cube = cube    
        self.caras = {}
        self.left_corner = []
        self.right_corner = []
        self.down_corner = []
        self.up_edge = []
        self.down_edge = []
        self.center = []
        
    def count_caras(self):
        return len(self.cube)
    
    def get_cube(self):
        return self.cube
    
    def get_faces(self):
        return self.caras
    

    def assemble(self):
        self.caras['front'] = self.cube[0]
        self.caras['right'] = self.cube[1]
        self.caras['left'] = self.cube[2]
        self.caras['back'] = self.cube[3]
        self.caras['down'] = self.cube[5]
        self.caras['up'] = self.cube[4]
      
    def show_faces(self):
        print("Current state of the cube:")
        for face, content in self.caras.items():
            print(face)
            for row in content:
                print(' '.join(row))
            print()  # Separador entre caras

    def get_left_Corner(self):
        return self.left_corner

    def intersections_left_corner(self, left_corner):
        #las esquinas tienen 3 colores:
        if not left_corner in self.left_corner:
            self.left_corner.append(left_corner)
    
    def intersections_right_corner(self, right_corner):
        #las esquinas tienen 3 colores:
        if not right_corner in self.right_corner:
            self.right_cornes.append(right_corner)
            
    def intersections_up_corner(self, up_edge):
        #las esquinas tienen 3 colores:
        if not up_edge in self.up_corner:
            self.up_edge.append(up_edge)
    
    def intersections_down_edge(self, down_edge):
        #las esquinas tienen 3 colores:
        if not down_edge in self.up_corner:
            self.down_edge.append(down_edge)        
    
    def center(self, center):
        if not center in self.center:
            self.center.append(center) 
        

    def show_cube(self,cube):
        for cara in cube:
            for row in cara:
                print(' '.join(row))
            print()  # Separador entre caras    
            
    #only face        
    def show_face(self, face):
        for row in self.caras[face]:
            print(' '.join(row))
    
    def get_goal_cube(self):
        goal_cube = [
                [['1W', '2W', '3W'],
                ['4W', '5W', '6W'],
                ['7W', '8W', '9W']],

                [['1G', '2G', '3G'],
                ['4G', '5G', '6G'],
                ['7G', '8G', '9G']],

                [['1B', '2B', '3B'],
                ['4B', '5B', '6B'],
                ['7B', '8B', '9B']],

                [['1Y', '2Y', '3Y'],
                ['4Y', '5Y', '6Y'],
                ['7Y', '8Y', '9Y']],

                [['1O', '2O', '3O'],
                ['4O', '5O', '6O'],
                ['7O', '8O', '9O']],

                [['1R', '2R', '3R'],
                ['4R', '5R', '6R'],
                ['7R', '8R', '9R']]
            ]
        return goal_cube
    
    