
# def transform_cube(cube):
#     for cara in cube:
           
 
# def validate_center_cube(cube):
#     center = cube[0][1][1]
#     center.left = cube[]
#     if center == 'W':
#         if center.left == 

def validate_cara(cube):
    if len(cube) != 6:
        print("Error: Invalid missing rubik's cube face")

def validate_color(cube):
    for cara in cube:
        for fila in cara:
            if len(fila) != 3:
                print("Error: invalid missing color")
                
                
class RubiksCube:
    def __init__(self, color):#cube
       self.color = color

    

    
    # def up(self):
    #     return  
    
    # def down(self):
    #     return 
    
    # def left(self, ):
    #     return  