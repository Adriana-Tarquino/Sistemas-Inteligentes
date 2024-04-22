from RubiksCube import RubiksCube, Validator
# strip() ->  Para elimnar espacios en blanco
# split() -> para dividt la linea en una lista de elementos 
#(si la linea esta vacia entonces quiere decir que termino una cara del cubo)

def load_file(nombre_archivo):
    cube = []
    cara = []

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco alrededor de la línea y verificar si es una cadena no vacía
            linea = linea.strip()
            if linea:  
                fila = linea.split()
                cara.append(fila)
            else:
                # Si la línea está vacía, agregamos la cara actual al cubo si tiene al menos una fila
                if cara:
                    cube.append(cara)
                    cara = []

    # Añadir la última cara si quedó pendiente
    if cara:
        cube.append(cara)
        
    return cube



if __name__ == "__main__":
   
   archivo = 'Cubo Rubik\\rubik_cube_file.txt'

   cube = load_file(archivo)
cuboe = RubiksCube(cube)
cuboe.assemble()
cuboe.rotate_face_clockwise('front') 
cuboe.show_face('front')  # Mostrar el estado actual del cubo
print("------------------------------------------------")
cuboe.rotate_face_counter_clockwise('front')  # Por ejemplo, rotar la cara frontal en sentido de las manecillas del reloj
cuboe.show_face('front')  # Mostrar el estado actual del cubo
   

      
          

