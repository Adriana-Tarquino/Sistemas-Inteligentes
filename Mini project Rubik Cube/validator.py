from rubiks_cube import RubiksCube

class Validator(object):

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
   
