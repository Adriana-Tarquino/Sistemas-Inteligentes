
class Validator(object):
    def __init__(self, cube):
        self.cube = cube
    
    def validate_cara(self):
        if self.cube.count_caras() != 6:
            print("Error: Invalid missing rubik's cube face")
            
    def validate_color(self):
        for cara in self.cube.get_cube():
            for fila in cara:
                if len(fila) != 3:
                    print("Error: invalid missing color")


class RubiksCube:
    def __init__(self, cube):#cube
        self.cube = cube
        self.front = cube[0]
        self.right = cube[1]
        self.left = cube[2]
        self.down = cube[3]
        self.up = cube[4]
        self.back = cube[5]
    
    #que pasa cuando no hay una cara esto trae porblemas
    
    def count_caras(self):
        return len(self.cube)
    
    def get_cube(self):
        return self.cube
    

    
 