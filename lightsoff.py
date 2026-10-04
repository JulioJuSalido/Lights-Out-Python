import sys
import msvcrt
import os
import random
import time
# LIGHTS OFF GAME - JULIO CESAR JU SALIDO

ancho_pixel = 50
alto = 24
espacio_x = 2
espacio_y = 1
inicio_x = 1
inicio_y = 10
pila_ayuda = []

def centrar(dificultad):
    global inicio_x
    tam = os.get_terminal_size()
    columnas = tam.columns
    
    ancho_tablero = (ancho_pixel * dificultad) + (espacio_x * (dificultad - 1))
    
    inicio_x = (columnas // 2) - (ancho_tablero // 2)

def dibujar_matriz(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):

            pos_x = inicio_x + x * (ancho_pixel + espacio_x)
            pos_y = inicio_y + y * (alto + espacio_y)

            if matriz[y][x] == 1:
                cls_establecer_color_hex("ffffff")
                girasol(pos_x,pos_y)
                cls_restaurar_colores()
            else:
                cls_establecer_color_hex("90d5ff")
                nogirasol(pos_x,pos_y)
                cls_restaurar_colores()

def imprimir(pos_x,pos_y,simbolo_luz):
    sys.stdout.write(f"\033[{pos_y};{pos_x}H")
    sys.stdout.write(simbolo_luz)
    sys.stdout.flush()

def crear_matriz(dificultad):
    matriz = []

    for i in range(dificultad):
        fila = []
        for j in range(dificultad):
            fila.append(0)
        matriz.append(fila)

    posicion = []

    for y in range(dificultad):
        for x in range(dificultad):
            posicion.append((y,x))

    luces = random.sample(posicion, 4)

    for y,x in luces:
        pila_ayuda.append((y,x))
        actualizar_tablero(matriz, y, x)

    return matriz
    
def titulo():    
    imprimir(inicio_x,1 ,"░██         ░██████  ░██████  ░██     ░██ ░██████████  ░██████        ░██████   ░██     ░██ ░██████████")
    imprimir(inicio_x,2 ,"░██           ░██   ░██   ░██ ░██     ░██     ░██     ░██   ░██      ░██   ░██  ░██     ░██     ░██    ")
    imprimir(inicio_x,3 ,"░██           ░██  ░██        ░██     ░██     ░██    ░██            ░██     ░██ ░██     ░██     ░██    ")
    imprimir(inicio_x,4 ,"░██           ░██  ░██  █████ ░██████████     ░██     ░████████     ░██     ░██ ░██     ░██     ░██    ")
    imprimir(inicio_x,5 ,"░██           ░██  ░██     ██ ░██     ░██     ░██            ░██    ░██     ░██ ░██     ░██     ░██    ")
    imprimir(inicio_x,6 ,"░██           ░██   ░██  ░███ ░██     ░██     ░██     ░██   ░██      ░██   ░██   ░██   ░██      ░██    ")
    imprimir(inicio_x,7 ,"░██████████ ░██████  ░█████░█ ░██     ░██     ░██      ░██████        ░██████     ░██████       ░██    ")

def iniciar_ascii():
    cls_establecer_color_hex("572364")
    imprimir(inicio_x,9 ,"██ ███    ██ ██  ██████ ██  █████  ██████           ██ ██    ██ ███████  ██████   ██████       ██ ███████ ███████ ██████   █████   ██████ ██  ██████  ██")                                                                                                                                                         
    imprimir(inicio_x,10 ,"██ ████   ██ ██ ██      ██ ██   ██ ██   ██          ██ ██    ██ ██      ██       ██    ██     ██  ██      ██      ██   ██ ██   ██ ██      ██ ██    ██  ██")
    imprimir(inicio_x, 11 ,"██ ██ ██  ██ ██ ██      ██ ███████ ██████           ██ ██    ██ █████   ██   ███ ██    ██     ██  █████   ███████ ██████  ███████ ██      ██ ██    ██  ██")
    imprimir(inicio_x,12 ,"██ ██  ██ ██ ██ ██      ██ ██   ██ ██   ██     ██   ██ ██    ██ ██      ██    ██ ██    ██     ██  ██           ██ ██      ██   ██ ██      ██ ██    ██  ██")
    imprimir(inicio_x,13 ,"██ ██   ████ ██  ██████ ██ ██   ██ ██   ██      █████   ██████  ███████  ██████   ██████       ██ ███████ ███████ ██      ██   ██  ██████ ██  ██████  ██")
    cls_restaurar_colores()                                                                                                                                        

def instruccion_dificultad():
    imprimir(inicio_x,9, "▄█████ ██████ ██     ██████ ▄█████ ▄█████ ██ ▄████▄ ███  ██ ██████   ████▄  ██ ██████ ██ ▄█████ ██  ██ ██    ██████ ▄████▄ ████▄      ▄██       ██████ ▄████▄ ▄█████ ██  ██      ████▄       ██▄  ▄██ ██████ ████▄  ██ ▄████▄       ████▄       ████▄  ██████ ██▄  ▄██ ▄████▄ ███  ██    ")
    imprimir(inicio_x,10,"▀▀▀▄▄▄ ██▄▄   ██     ██▄▄   ██     ██     ██ ██  ██ ██ ▀▄██ ██▄▄     ██  ██ ██ ██▄▄   ██ ██     ██  ██ ██      ██   ██▄▄██ ██  ██ ▀    ██   ▄▄▄ ██▄▄   ██▄▄██ ▀▀▀▄▄▄  ▀██▀ ▄▄▄    ▄██▀   ▄▄▄ ██ ▀▀ ██ ██▄▄   ██  ██ ██ ██  ██ ▄▄▄    ▄▄██   ▄▄▄ ██  ██ ██▄▄   ██ ▀▀ ██ ██  ██ ██ ▀▄██ ▄▄▄ ")
    imprimir(inicio_x,11,"█████▀ ██▄▄▄▄ ██████ ██▄▄▄▄ ▀█████ ▀█████ ██ ▀████▀ ██   ██ ██▄▄▄▄   ████▀  ██ ██     ██ ▀█████ ▀████▀ ██████  ██   ██  ██ ████▀  ▄    ██       ██▄▄▄▄ ██  ██ █████▀   ██   ▄    ███▄▄       ██    ██ ██▄▄▄▄ ████▀  ██ ▀████▀  ▄    ▄▄▄█▀       ████▀  ██▄▄▄▄ ██    ██ ▀████▀ ██   ██     ")

def victoria_ascii(dificultad):                                      
    imprimir(inicio_x,(dificultad*25)+16,"    ▄   ▄▄▄▄     ▄▄       ▄▄     ▄▄▄    ▄▄      ▄▄▄▄▄     ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄  ▄▄")
    imprimir(inicio_x,(dificultad*25)+17,"    ▀██████▀   ▄█▀▀█▄     ██▄   ██▀   ▄█▀▀█▄   ██▀▀▀▀█▄  █▀▀██▀▀▀▀  █▀██▀▀▀   ██")
    imprimir(inicio_x,(dificultad*25)+18,"██    ██   ▄   ██  ██     ███▄  ██    ██  ██   ▀██▄  ▄▀     ██        ██      ██")
    imprimir(inicio_x,(dificultad*25)+19,"      ██  ██   ██▀▀██     ██ ▀█▄██    ██▀▀██     ▀██▄▄      ██        ████    ██")
    imprimir(inicio_x,(dificultad*25)+20,"██    ██  ██ ▄ ██  ██     ██   ▀██  ▄ ██  ██   ▄   ▀██▄     ██        ██        ")
    imprimir(inicio_x,(dificultad*25)+21,"██    ▀█████ ▀██▀  ▀█▄█ ▀██▀    ██  ▀██▀  ▀█▄█ ▀██████▀     ▀██▄      ▀█████  ██")
    imprimir(inicio_x,(dificultad*25)+22,"██")

def activo_ascii(dificultad):
    imprimir(inicio_x,(dificultad*25)+16,"     ▄▄    ▄   ▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄  ▄▄▄          ▄▄▄▄")
    imprimir(inicio_x,(dificultad*25)+17,"   ▄█▀▀█▄  ▀██████▀  █▀▀██▀▀▀▀  █▀ ██   █▀██  ██▀▀  ▄█▀▀████▄")
    imprimir(inicio_x,(dificultad*25)+18,"   ██  ██    ██         ██         ██     ██  ██    ██    ██")
    imprimir(inicio_x,(dificultad*25)+19,"   ██▀▀██    ██         ██         ██     ██  ██    ██    ██")
    imprimir(inicio_x,(dificultad*25)+20," ▄ ██  ██    ██         ██         ██     ██▄ ██    ██    ██")
    imprimir(inicio_x,(dificultad*25)+21," ▀██▀  ▀█▄█  ▀█████     ▀██▄     ▄▄██▄▄    ▀███▀     ▀████▀")

def borrar_activo(dificultad):
    for x in range(6):
        imprimir(inicio_x,((dificultad*25)+16) + x,"                                                            ")

def derrota_ascii(dificultad):
    imprimir(inicio_x,(dificultad*25)+16,"    ▄▄")
    imprimir(inicio_x,(dificultad*25)+17," █▀██▀▀▀█▄  █▀██▀▀▀   █▀██▀▀▀█▄  █▀██▀▀██   █▀ ██   ██▀▀▀▀█▄  █▀▀██▀▀▀▀  █▀██▀▀▀")
    imprimir(inicio_x,(dificultad*25)+18,"   ██▄▄▄█▀    ██        ██▄▄▄█▀    ██   ██     ██   ▀██▄  ▄▀     ██        ██")
    imprimir(inicio_x,(dificultad*25)+19,"   ██▀▀▀      ████      ██▀▀█▄     ██   ██     ██     ▀██▄▄      ██        ████")
    imprimir(inicio_x,(dificultad*25)+20," ▄ ██         ██      ▄ ██  ██   ▄ ██   ██     ██   ▄   ▀██▄     ██        ██")
    imprimir(inicio_x,(dificultad*25)+20," ▀██▀         ▀█████  ▀██▀  ▀██▀ ▀██▀███▀    ▄▄██▄▄ ▀██████▀     ▀██▄      ▀█████")

def instruccion_controles():
    imprimir(inicio_x,9, " ▄   ▄▄▄▄                          ▄▄                    ▄▄▄▄▄▄▄ ▄▄                                   ▄█   ▄▄▄     ▄▄▄                          █▄         ▄▄▄▄▄▄▄   ▄▄     ▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄   ▄▄▄▄▄▄       ▄█   ▄▄▄▄▄▄                                                      █▄         ▄▄▄▄▄▄▄   ▄▄▄▄▄     ▄▄▄▄▄▄      ▄▄    ▄   ▄▄▄▄   ▄▄▄▄▄▄   ▄▄▄▄        ▄█   ▄▄▄     ▄▄▄                                                    █▄          ▄▄▄▄        ▄█   ▄▄▄▄▄        ▄▄           █▄")
    imprimir(inicio_x,10," ▀██████▀             █▄            ██                  █▀██▀▀▀   ██             █▄                  ██     ███▄ ▄███                            ██       █▀██▀▀▀    ██▄   ██▀   █▀▀██▀▀▀▀  █▀██▀▀▀   █▀██▀▀▀█▄    ██   █▀ ██         █▄                        █▄                    ██       █▀██▀▀▀   ██▀▀▀▀█▄  █▀██▀▀▀█▄  ▄█▀▀█▄  ▀██████▀  █▀ ██   ▄█▀▀████▄    ██     ███▄ ▄███            █▄                              █▄        ██       ▄█▀▀███▄▄    ██   ██▀▀▀▀█▄       ██           ██")
    imprimir(inicio_x,11,"   ██           ▄    ▄██▄▄          ██                    ██      ██             ██                  ██     ██ ▀█▀ ██                     ▄      ██         ██       ███▄  ██       ██        ██        ██▄▄▄█▀    ██      ██   ▄    ▄██▄      ▄               ▄██▄            ▄      ██         ██      ▀██▄  ▄▀    ██▄▄▄█▀  ██  ██    ██         ██   ██    ██     ██     ██ ▀█▀ ██            ██                              ██        ██       ██    ██     ██   ▀██▄  ▄▀       ██ ▀▀ ▄      ██")
    imprimir(inicio_x,12,"   ██     ▄███▄ ████▄ ██ ████▄▄███▄ ██ ▄█▀█▄ ▄██▀█ ▀      ███▀    ██ ▄█▀█▄ ▄███▀ ████▄ ▄▀▀█▄ ▄██▀█   ██     ██     ██   ▄███▄▀█▄ ██▀▄█▀█▄ ████▄  ██         ████     ██ ▀█▄██       ██        ████      ██▀▀█▄     ██      ██   ████▄ ██ ▄█▀█▄ ████▄▄▀▀█▄ ▄███▀ ██ ██ ██ ▄▀▀█▄ ████▄  ██         ████      ▀██▄▄     ██▀▀▀    ██▀▀██    ██         ██   ██    ██     ██     ██     ██   ▄███▄ ▄████ ▄███▄   ▄▀▀█▄ ██ ██ ██ ██ ▄████ ▄▀▀█▄  ██       ██    ██     ██     ▀██▄▄  ▄▀▀█▄ ██ ██ ████▄  ██")
    imprimir(inicio_x,13,"   ██     ██ ██ ██ ██ ██ ██   ██ ██ ██ ██▄█▀ ▀███▄      ▄ ██      ██ ██▄█▀ ██    ██ ██ ▄█▀██ ▀███▄   ██     ██     ██   ██ ██ ██▄██ ██▄█▀ ██     ██         ██       ██   ▀██       ██        ██      ▄ ██  ██     ██      ██   ██ ██ ██ ██▄█▀ ██   ▄█▀██ ██    ██ ██ ██ ▄█▀██ ██     ██         ██      ▄   ▀██▄  ▄ ██     ▄ ██  ██    ██         ██   ██    ██     ██     ██     ██   ██ ██ ██ ██ ██ ██   ▄█▀██ ██▄██ ██ ██ ██ ██ ▄█▀██  ██       ██  ▄ ██     ██   ▄   ▀██▄ ▄█▀██ ██ ██ ██     ██")
    imprimir(inicio_x,14,"   ▀█████▄▀███▀▄██ ▀█▄██▄█▀  ▄▀███▀▄██▄▀█▄▄▄█▄▄██▀ ▄    ▀██▀     ▄██▄▀█▄▄▄▄▀███▄▄██ ██▄▀█▄███▄▄██▀   ██   ▀██▀     ▀██▄▄▀███▀  ▀█▀ ▄▀█▄▄▄▄█▀     ██  ▄      ▀█████ ▀██▀    ██       ▀██▄      ▀█████  ▀██▀  ▀██▀   ██    ▄▄██▄▄▄██ ▀█▄██▄▀█▄▄▄▄█▀  ▄▀█▄██▄▀███▄▄██▄▀██▀█▄▀█▄██▄█▀     ██  ▄      ▀█████  ▀██████▀  ▀██▀     ▀██▀  ▀█▄█  ▀█████   ▄▄██▄▄  ▀████▀      ██   ▀██▀     ▀██▄▄▀███▀▄█▀███▄▀███▀  ▄▀█▄██▄▄▀██▀▄▀██▀█▄█▀███▄▀█▄██  ██  ▄     ▀█████▄     ██   ▀██████▀▄▀█▄██▄██▄██▄█▀     ██")
    imprimir(inicio_x,15,"                                                                                                      ▀█                                        █▀  ▄█                                                              ▀█                                                               █▀  ▄█                                                                           ▀█                                            ██                    █▀  ▄█          ▀█      ▀█                             █▀")
    
def cls_imprimir(texto):
    """Imprime texto inmediatamente en pantalla sin hacer salto de línea."""
    sys.stdout.write(texto)
    sys.stdout.flush()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def cls_mover_cursor(fila, columna):
    """Mueve el cursor a una posición específica de la terminal."""
    cls_imprimir(f"\033[{fila};{columna}H")

def cls_ocultar_cursor():
    """Oculta el cursor parpadeante."""
    cls_imprimir("\033[?25l")

def cls_mostrar_cursor():
    """Muestra nuevamente el cursor."""
    cls_imprimir("\033[?25h")

def cls_limpiar_pantalla():
    """Borra todo el contenido de la consola."""
    sys.stdout.write(f"\033[2J\033[H")
    sys.stdout.flush()

def cls_restaurar_colores():
    """Vuelve a los colores por defecto de la terminal."""
    cls_imprimir("\033[0m")

def cls_establecer_color_hex(hex_color):
    """
    Toma un color hexadecimal y aplica color 'True Color' (24 bits)
    al texto de la consola usando el código ANSI: \033[38;2;R;G;Bm
    """
    # 1. Convertir Hex (base 16) a RGB (base 10).
    # [0:2] toma los primeros dos caracteres, int(..., 16) lo convierte a entero base 10
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # 2. Aplicar el código ANSI True Color.
    cls_imprimir(f"\033[38;2;{r};{g};{b}m")

def cls_leer_tecla():
    """
    Lee la tecla y la traduce.
    """
    if not msvcrt.kbhit(): # Esperar a que el usuario presione alguna tecla.
        pass 
    
    tecla = msvcrt.getch()

    # Detectar ENTER.
    if tecla == b'\r':
        return "ENTER"

    # Detectar Flechas (son códigos de dos bytes).
    if tecla in (b'\x00', b'\xe0'):
        flecha = msvcrt.getch()
        if flecha == b'H': return "ARRIBA"
        if flecha == b'P': return "ABAJO"
        if flecha == b'M': return "DERECHA"
        if flecha == b'K': return "IZQUIERDA"
        
    if tecla == b'1':
        return "UNO"
    if tecla == b'2':
        return "DOS"
    if tecla == b'3':
        return "TRES"
    
    if tecla.lower() == b'h':
        return "H"
    
    # Detectar SALIR.
    if tecla.lower() == b'q' or tecla == b'\x1b':
        return "SALIR"

    if tecla == b' ':
        return "ESPACIO"

    return "OTRA"


# ==========================================
# LÓGICA DEL JUEGO
# ==========================================

def victoria(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):

            if matriz[y][x] == 1:
                return False

    return True

def actualizar_tablero(matriz, fila, columna):
    tamaño = len(matriz)

    #Esto es para hacer el cambio de luz profe
    if matriz[fila][columna] == 1:
        matriz[fila][columna] = 0
    else:
        matriz[fila][columna] = 1

    #Vecino de arriba
    if fila > 0:
        if matriz[fila-1][columna] == 1:
            matriz[fila-1][columna] = 0
        else:
            matriz[fila-1][columna] = 1

    #Vecino de abajo
    if fila < tamaño - 1:
        if matriz[fila+1][columna] == 1:
            matriz[fila+1][columna] = 0
        else:
            matriz[fila+1][columna] = 1

    #Vecino izquierdo
    if columna > 0:
        if matriz[fila][columna-1] == 1:
            matriz[fila][columna-1] = 0
        else:
            matriz[fila][columna-1] = 1

    #Vecino derecho
    if columna < tamaño - 1:
        if matriz[fila][columna+1] == 1:
            matriz[fila][columna+1] = 0
        else:
            matriz[fila][columna+1] = 1

def dibujar_personaje(fila, columna, matriz, color):
    fila -= 1
    columna -= 1

    pos_x = inicio_x + columna * (ancho_pixel + espacio_x)
    pos_y = inicio_y + fila * (alto + espacio_y)

    cls_establecer_color_hex(color)

    if matriz[fila][columna] == 1:
        girasol(pos_x, pos_y)
    else:
        nogirasol(pos_x, pos_y)

    cls_restaurar_colores()
    
def borrar_rastro(fila, columna, matriz):
    fila -= 1
    columna -= 1

    pos_x = inicio_x + columna * (ancho_pixel + espacio_x)
    pos_y = inicio_y + fila * (alto + espacio_y)

    if matriz[fila][columna] == 1:
        cls_establecer_color_hex("ffffff")
        girasol(pos_x, pos_y)
        cls_restaurar_colores()
    else:
        cls_establecer_color_hex("90d5ff")
        nogirasol(pos_x, pos_y)
        cls_restaurar_colores

def girasol(pos_x,pos_y,):
    imprimir(pos_x + 23, pos_y + 5,"######")
    imprimir(pos_x + 15, pos_y + 6,"########::::::########")
    imprimir(pos_x + 13, pos_y + 7,"##::::::##------##::::::##")
    imprimir(pos_x + 9, pos_y + 8,"######----##############----######")
    imprimir(pos_x + 7, pos_y + 9,"##::::######--------------######::::##")
    imprimir(pos_x + 5, pos_y + 10,"####----##----------------------##----####")
    imprimir(pos_x + 2, pos_y + 11,":##::######--------++++++++++++++----######::##:")
    imprimir(pos_x + 1, pos_y + 12,"++--::-=##==--======++++++++++++++======##=-::--++")
    imprimir(pos_x + 1, pos_y + 13,"##------##--==++++%%%%++++++++%%%%++++==##------##")
    imprimir(pos_x + 1, pos_y + 14,"++======*+-=++++++@@**++++++++@@**++++++**+=====++")
    imprimir(pos_x + 1, pos_y + 15,":-****##--++++++++@@:-=+++++++@@--++++++++##****-:")
    imprimir(pos_x + 1, pos_y + 16,"##----##--++++++++@@@@++++++++@@@@++++++++##----##")
    imprimir(pos_x + 1, pos_y + 17,"##::::##--++++++++@@@@++++++++@@@@++++++++##::::*#")
    imprimir(pos_x + 2, pos_y + 18,":######++++++++++++++++++++++++++++++++**######:")
    imprimir(pos_x + 1, pos_y + 19,"##------##++++@@@@++++++++++++++++@@++**##------##")
    imprimir(pos_x + 1, pos_y + 20,"##::::::##++++++++@@@@@@@@@@@@@@@@++****##::::::*#")
    imprimir(pos_x + 2, pos_y + 21,":##::######++++++++********@@@@******######::##:")
    imprimir(pos_x + 5, pos_y + 22,"####----##****++++++++**********##----####")
    imprimir(pos_x + 7, pos_y + 23,"##::::######**************######::::##")
    imprimir(pos_x + 9, pos_y + 24,"######----##############----######")
    imprimir(pos_x + 9, pos_y + 25,"::::##::::--##======##--::::##::::")
    imprimir(pos_x + 13, pos_y + 26,"::******##::::::##******:")
    imprimir(pos_x + 15, pos_y + 27,"======##++++++##======")

def nogirasol(pos_x,pos_y):
    imprimir(pos_x + 23, pos_y + 5,"######")
    imprimir(pos_x + 15, pos_y + 6,"########::::::########")
    imprimir(pos_x + 13, pos_y + 7,"##::::::##------##::::::##")
    imprimir(pos_x + 9, pos_y + 8,"######----##############----######")
    imprimir(pos_x + 7, pos_y + 9,"##::::######--------------######::::##")
    imprimir(pos_x + 5, pos_y + 10,"####----##----------------------##----####....")
    imprimir(pos_x + 2, pos_y + 11,":##::######--------------------------######::##")
    imprimir(pos_x + 1, pos_y + 12,"++--::-=##------------------------------##=-::--++")
    imprimir(pos_x + 1, pos_y + 13,"##------##------------------------------##------##")
    imprimir(pos_x + 1, pos_y + 14,"++======*-------------------------------**+=====++")
    imprimir(pos_x + 1, pos_y + 15,":-****##----------------------------------##****-:")
    imprimir(pos_x + 1, pos_y + 16,"##----##----------------------------------##----##")
    imprimir(pos_x + 1, pos_y + 17,"##::::##----------------------------------##::::*#")
    imprimir(pos_x + 2, pos_y + 18,":######----------------------------------######:")
    imprimir(pos_x + 1, pos_y + 19,"##------##------------------------------##------##")
    imprimir(pos_x + 1, pos_y + 20,"##::::::##------------------------------##::::::*#")
    imprimir(pos_x + 2, pos_y + 21,":##::######--------------------------######::##:")
    imprimir(pos_x + 5, pos_y + 22,"####----##----------------------##----####")
    imprimir(pos_x + 7, pos_y + 23,"##::::######--------------######::::##")
    imprimir(pos_x + 9, pos_y + 24,"######----##############----######")
    imprimir(pos_x + 9, pos_y + 25,"::::##::::--##======##--::::##::::")
    imprimir(pos_x + 13, pos_y + 26,"::******##::::::##******:")
    imprimir(pos_x + 15, pos_y + 27,"======##++++++##======")


def juego():
    clear()
    centrar(7)
    titulo()
    iniciar_ascii()
    while True:
        comando = cls_leer_tecla()
        if comando == "ESPACIO":
            clear()
            break
        elif comando == "SALIR":
            return
        else:
            continue
    titulo()
    instruccion_dificultad()
    while True:
        comando = cls_leer_tecla()
        if comando == "UNO":
            dificultad = 5
            break
        elif comando == "DOS":
            dificultad = 7
            break
        elif comando == "TRES":
            dificultad = 9
            break
        elif comando == "SALIR":
            return
        else:
            continue   
    clear()
    centrar(dificultad)
    matriz = crear_matriz(dificultad)
    titulo()
    instruccion_controles()
    dibujar_matriz(matriz)
    activo_ascii(dificultad)
    
    fila = 1
    columna = 1
    color = "ffa500"
    dibujar_personaje(fila,columna,matriz,color)
    try:
        while True:
            comando = cls_leer_tecla()
            # LÓGICA DE MOVIMIENTO.
            fila_ant, col_ant = fila, columna

            if comando == "ARRIBA":
                fila = max(1, fila - 1)

            elif comando == "ABAJO":
                fila = min(dificultad, fila + 1)

            elif comando == "DERECHA":
                columna = min(dificultad, columna + 1)

            elif comando == "IZQUIERDA":
                columna = max(1, columna - 1)
               
            elif comando == "ESPACIO":
                if len(pila_ayuda) > 0:
                    fila_inicio = fila
                    columna_inicio = columna
                    
                    tempy,tempx = pila_ayuda[-1]
                    fila = tempy + 1
                    columna = tempx + 1
                    color = "ff0000"
                    dibujar_personaje(fila, columna, matriz, color)  
                    
                    fila = fila_inicio
                    columna = columna_inicio
                    color = "ffa500"
                    dibujar_personaje(fila, columna, matriz,color) 
                    
            elif comando == "ENTER":
                actualizar_tablero(matriz, fila-1, columna-1)
                dibujar_matriz(matriz)
                color = "ffa500"
                dibujar_personaje(fila, columna, matriz,color)
                
                confirmacion = victoria(matriz)
                
                if confirmacion == True:
                    borrar_activo(dificultad)
                    victoria_ascii(dificultad)
                    break
                
                if len(pila_ayuda) > 0:
                    tempy = fila - 1
                    tempx = columna - 1
                    y,x = pila_ayuda[-1]
                    if  (tempy,tempx) == (y,x):
                        pila_ayuda.pop()
                    else:
                        pila_ayuda.append((tempy,tempx))
            
            elif comando == "SALIR":
                borrar_activo(dificultad)
                derrota_ascii(dificultad)
                break
            
            else:
                continue

            if fila != fila_ant or columna != col_ant:
                borrar_rastro(fila_ant, col_ant, matriz)
                color = "ffa500"
                dibujar_personaje(fila, columna, matriz, color)
    finally:
        cls_mover_cursor((dificultad*25)+24,1)
        print("Juego cerrado.")
    
if __name__ == "__main__":
    juego() 