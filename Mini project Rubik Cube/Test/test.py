import unittest

class TestMatrizTridimensional(unittest.TestCase):
    
    # Definimos la función que crea la matriz tridimensional
    def crear_matriz_tridimensional(self):
        cubo_data = [
            [['1B', '2B', '3B'],
             ['4W', '5W', '6W'],
             ['7W', '8W', '9W']],

            [['1W', '2W', '3W'],
             ['4G', '5G', '6G'],
             ['7G', '8G', '9G']],

            [['1Y', '2Y', '3Y'],
             ['4B', '5B', '6B'],
             ['7B', '8B', '9B']],

            [['1G', '2G', '3G'],
             ['4Y', '5Y', '6Y'],
             ['7Y', '8Y', '9Y']],

            [['1O', '2O', '3O'],
             ['4O', '5O', '6O'],
             ['7O', '8O', '9O']],

            [['1R', '2R', '3R'],
             ['4R', '5R', '6R'],
             ['7R', '8R', '9R']]
        ]
        return cubo_data

    def test_creacion_matriz_tridimensional(self):
        matriz = self.crear_matriz_tridimensional()
        self.assertEqual(len(matriz), 6)  
        for cara in matriz:
            self.assertEqual(len(cara), 3) 
            for fila in cara:
                self.assertEqual(len(fila), 3)  

if __name__ == '__main__':
    unittest.main()
