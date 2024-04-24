# Sistemas-Inteligentes
# Reporte Técnico

# 1. Autor(a)
    Autor: Adriana Valentina Tarquino Cespedes

## 2. Breve Descripción del Proyecto
El proyecto consiste en el desarrollo de una busqueda de resolución del Cubo Rubik de manera optima utilizando técnicas de busqueda informada.

## 3. Requerimientos del Entorno de Programación
- Lenguaje de programación: Python 3.7 o superior
- Se importa una libreria `PriorityQueue` desde el módulo queue. Este tipo de cola de prioridad se utiliza para almacenar los estados del cubo a medida que se realiza la búsqueda.

## 4. Manual de Uso

### 4.1 Formato de Codificación para Cargar el Estado de un Cubo desde el Archivo de Texto
El estado del cubo se codificará en un archivo de texto con el siguiente formato:
```
W W W
W W W
W W W

G G G
G G G
G G G

B B B
B B B
B B B

Y Y Y
Y Y Y
Y Y Y

O O O
O O O
O O O

R R R
R R R
R R R

```
Donde cada letra representa el color de una cara del cubo:
                W = white (blanco)
                G = Green (verde)
                B = Blue (Azul)
                Y = Yellow(Amarillo)
                O = Orange(Naranja)
                R = Red (Rojo)

### 4.2 Instrucciones para Ejecutar el Programa
1. Clonar el repositorio desde Github.
2. Ejecutar el programa principal mediante `python -u "Mini project Rubik Cube\main.py"`.
3. Seleccionar la opción de  `Validate Cube` el estado del cubo desde un archivo de texto.
4. Seleccionar la opción de su preferencia, para validar el cubo
5. Volver al menu principal.
6. Seleccionar la opción de Disassemble Cube para desarmar el cubo
7. Seleccionar la opción de Calculate Manhattan Distance
8. Seleccionar la opción de Solve Cube, esperar a que el programa resuelva el cubo.
6. Se mostrará la solución en caso de no llegar a ala solucion se muestra un mensaje de Error.

## 5. Diseño e Implementación

### 5.1 Breve Descripción del Modelo del Problema
El problema se modela como la búsqueda optima de una secuencia de movimientos que lleven el cubo Rubik desde un estado inicial (desarmado) hasta un estado objetivo (armado), donde todas las caras estén formadas por un solo color.


### 5.2 Explicación y Justificación de Algoritmo(s), Técnicas, Heurísticas Seleccionadas

El diseño e implementación del modelo es representar un cubo de Rubik en una matriz tridimensional, asi como definir los movimientos U, U', R, R', L, L',D, D'. Se uso el `Algoritmo de A*`, con una heursitica la `distancia de Manhattan`, esto entre el estado actual del cubo y el estado objetivo.Esta elección se justifica por su eficacia y eficiencia en la resolución de problemas de búsqueda en espacios de estados grandes como el del cubo Rubik.

    - Algoritmo A:*Es un algoritmo de búsqueda informada que combina búsqueda exhaustiva y heurística para encontrar la solución óptima de manera eficiente. Utiliza una función de evaluación que considera tanto el costo acumulado para llegar a un estado como una estimación del costo restante hasta la meta

    - Heurística de Distancia de Manhattan: Estima el número mínimo de movimientos necesarios para alcanzar el estado objetivo desde el estado actual. Se calcula sumando las distancias horizontales y verticales entre las posiciones actuales y las posiciones objetivo de cada pieza del cubo.

## 6. Trabajo Futuro

### 6.1 Lista de Tareas Inconclusas y/o Ideas para Continuar con el Proyecto
- Implementación de una solución optima
- Implementación de paso a paso lo que el algoritmo debe ejecutar
- Mejora del algoritmo de A*
- Extender el programa para resolver cubos de dimensiones mayores.
