from rubiks_cube import RubiksCube
from validator import Validator
from moves_cube import *
from assamble import *

# strip() ->  Para elimnar espacios en blanco
# split() -> para dividt la linea en una lista de elementos 
#(si la linea esta vacia entonces quiere decir que termino una cara del cubo)
def load_file(nombre_archivo):
    cube = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]

    with open(nombre_archivo, 'r') as archivo:
        current_face = 0
        current_row = 0
        for linea in archivo:
            fila = linea.strip().split()
            if not fila:
                current_face += 1
                current_row = 0
            else:
                cube[current_face][current_row] = fila
                current_row += 1

    return cube


def validate_cube_menu(cube):
    validator = Validator(cube)
    while True:
        print("\nValidation Menu:")
        print("1. Validate Cube")
        print("2. Validate Adjacents")
        print("3. Validate Center")
        print("4. Validate Color")
        print("5. Validate Dimensions")
        print("6. Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            validator.validate_cara()
        elif choice == "2":
            validator.validate_adjacents()
        elif choice == "3":
            validator.validate_center()
        elif choice == "4":
            validator.validate_color()
        elif choice == "5":
            validator.validate_dimensions()
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main_menu():
    cube = load_file(archivo)
    Cubo_R = RubiksCube(cube)
    
    while True:
        print("\nMain Menu:")
        print("1. Disassemble Cube")
        print("2. Validate Cube")
        print("3. Calculate Manhattan Distance")
        print("4. Solve Cube")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            cubo_mov = Moves(Cubo_R)
            cubo_mov.U()
            cubo_mov.get_faces()
            
        elif choice == "2":
            Cubo_R.show_cube()
            validate_cube_menu(Cubo_R)
            
        elif choice == "3":
            cubo_mov = Moves(Cubo_R)
            distance = cubo_mov.manhattan_distance(Cubo_R.get_cube())
            print(f"\nDistance: {distance}")
            
        elif choice == "4":
            cubo_mov = Moves(Cubo_R)
            solution = cubo_mov.solve()
            if solution:
                print("\nSolution Steps:")
                for step, move in solution:
                    print(f"Step {step}: {move}")
            else:
                print("\nNo solution found.")
                
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    archivo = 'Mini project Rubik Cube\\Files\\rubik_cube_file_2.txt'
    main_menu()
