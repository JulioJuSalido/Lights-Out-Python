# Lights Out - Python
Juego de Lights Out desarrollado en Python para ejecutarse directamente en la terminal. El objetivo es apagar todas las luces del tablero utilizando el movimiento del jugador y activando o desactivando las casillas.

<img width="592" height="300" alt="image" src="https://github.com/user-attachments/assets/c13ce803-eb14-4a3d-bcf1-40613417a901" />

<img width="731" height="147" alt="image" src="https://github.com/user-attachments/assets/6cf607e6-204d-4a84-bda7-6ad4e0423dd8" />

<img width="502" height="510" alt="image" src="https://github.com/user-attachments/assets/0192ef81-cf9c-4d97-9ae7-352143f0b586" />

## Descripción
El juego presenta un tablero de diferentes tamaños donde algunas luces comienzan encendidas. Al seleccionar una casilla, esta cambia de estado junto con sus casillas vecinas.
El objetivo es lograr que **todas las luces del tablero queden apagadas**.

## Dificultades
El juego cuenta con tres tamaños de tablero:

| Opción | Tamaño |
| ------ | ------ |
| `1`    | 5 × 5  |
| `2`    | 7 × 7  |
| `3`    | 9 × 9  |

## Controles
| Tecla       | Acción                         |
| ----------- | ------------------------------ |
| `↑`         | Mover hacia arriba             |
| `↓`         | Mover hacia abajo              |
| `←`         | Mover hacia la izquierda       |
| `→`         | Mover hacia la derecha         |
| `ENTER`     | Activar/desactivar una casilla |
| `ESPACIO`   | Mostrar una posición de ayuda  |
| `Q` / `ESC` | Salir                          |

## Tecnologías utilizadas
* **Python**
* `msvcrt` para la lectura de teclas.
* `os` para controlar elementos de la terminal.
* `random` para generar las posiciones iniciales.
* Códigos **ANSI** para colores y posicionamiento.
* Caracteres ASCII para representar la interfaz del juego.

## Requisitos
Se necesita tener instalado:

* Python 3.x
* Sistema Windows, debido al uso de `msvcrt`.

No es necesario instalar librerías externas.

## Funcionamiento
El tablero se representa mediante una matriz de valores:

* `0` → luz apagada
* `1` → luz encendida

Cuando se activa una casilla, se cambia su estado y también el de sus vecinos:

* Arriba
* Abajo
* Izquierda
* Derecha

El juego termina cuando todas las posiciones de la matriz tienen el valor `0`.
