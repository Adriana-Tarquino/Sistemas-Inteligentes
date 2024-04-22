from rubiks_cube import RubiksCube
from validator import Validator
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


def print_menu():
    cube = load_file(archivo)
    Cubo_R = RubiksCube(cube)
    validator = Validator(Cubo_R)
    print("1. Validate Cube")
    print("2. Validate adjacents")
    print("3. Validate center")
    print("4. Validate color")
    print("5. Validate dimensions")
    print("6. Exit")
    while True:
        print("\nRubik's Cube Validation Menu:")
        choice = input("Enter your choice: ")
        if choice == "1":
            validator.validate_cara()
            break
        elif choice == "2":
            validator.validate_adjacents()
        elif choice == "3":
            validator.validate_center()
        elif choice == "4":
            validator.validate_color()
        elif choice == "5":
            validator.validate_dimensions()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    
    archivo = 'Cubo Rubik\\rubik_cube_file_2.txt'
    # print_menu()    
    cube = load_file(archivo)
    Cubo_R = RubiksCube(cube)
    
    # Cubo_R.assemble()
    print("------------------------------------------------")
    # print(Cubo_R.U())
    # Cubo_R.show_cube()
    Cubo_R.intersections_edge()
    

        
            

