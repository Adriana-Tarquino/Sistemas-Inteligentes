from RubiksCube import RubiksCube
# strip() ->  Para elimnar espacios en blanco
# split() -> para dividt la linea en una lista de elementos 
#(si la linea esta vacia entonces quiere decir que termino una cara del cubo)

def load_file(nombre_archivo):
    cube = []
    cara = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            if not fila:
                cube.append(cara)
                cara = []
            else:
                cara.append(fila)

    cube.append(cara)  

    return cube

if __name__ == "__main__":
   
   archivo = 'Cubo Rubik\\rubik_cube_file.txt'

   cube = load_file(archivo)

   for cara in cube:
      for fila in cara:
         print(' '.join(fila))
      print()  # Separador entre caras
    
   #  cube = [ 
   #          #white up
   #           [ ['W','W','W'],
   #             ['W','W','W'],
   #             ['W','W','W']  ],
   #          #green front
   #           [ ['G','G','G'],
   #             ['G','G','G'],
   #             ['G','G','G']  ],
   #          #red right
   #          [  ['R','R','R'],
   #             ['R','R','R'],
   #             ['R','R','R']  ],
   #          #blue back
   #          [  ['B','B','B'],
   #             ['B','B','B'],
   #             ['B','B','B']  ],
   #          #orange left
   #          [  ['O','O','O'],
   #             ['O','O','O'],
   #             ['O','O','O']  ],
   #          #yelow down
   #          [  ['Y','Y','Y'],
   #             ['Y','Y','Y'],
   #             ['Y','Y','Y']  ],
            
   #          ]
   #  RubiksCube(cube)
    
    