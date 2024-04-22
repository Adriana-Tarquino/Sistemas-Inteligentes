
class Validator(object):
    def __init__(self, cube):
        self.cube = cube
    
    def validate_Center(self):
        #cara, row, center
        cube = self.cube.get_cube()
        for i in range(len(cube)-1):
            if cube[i][1][1] == cube[i+1][1][1]:
                print("Error: Invalid Center in face", cube[i][1][1])        
        
       
    def validate_cara(self):
        if self.cube.count_caras() != 6:
            print("Error: Invalid missing rubik's cube face")
            
    def validate_color(self):
        for cara in self.cube.get_cube():
            for row in cara:
                if len(row) != 3:
                    print("Error: invalid missing color", row)


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
        
    def show_cube(self):
        for cara in self.cube:
            for row in cara:
                print(' '.join(row))
            print()  # Separador entre caras    
        
        
        

    
 