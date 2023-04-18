#Importamos el módulo pygame para utilizar sus funciones y clases
import pygame
#Importamos el módulo time para utilizar la función time.sleep() más adelante
import time
#Importamos el módulo random para generar números aleatorios más adelante
import random

#Inicializamos pygame
pygame.init()
 
 #Definimos algunos colores utilizando el modelo RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
#Definimos las dimensiones de la ventana de juego
dis_width = 600
dis_height = 400
 
#Creamos la ventana de juego utilizando las dimensiones definidas anteriormente
dis = pygame.display.set_mode((dis_width, dis_height))

#Le damos un nombre a la ventana de juego
pygame.display.set_caption('Snake Game')

#Creamos un objeto Clock que utilizaremos más adelante para controlar la velocidad del juego
clock = pygame.time.Clock()
 
#Definimos el tamaño de los bloques de la serpiente
snake_block = 10

#Definimos la velocidad de la serpiente
snake_speed = 15
 
#Definimos el estilo de fuente que utilizaremos para el texto en pantalla 
font_style = pygame.font.SysFont("bahnschrift", 25)

#Definimos el estilo de fuente que utilizaremos para mostrar la puntuación en pantalla
score_font = pygame.font.SysFont("comicsansms", 35)
 
#Esta función recibe la puntuación actual del jugador como argumento
def Your_score(score):
#Creamos un objeto Surface con el texto "Your Score: " y la puntuación actual del jugador
    value = score_font.render("Your Score: " + str(score), True, yellow)

#Dibujamos el objeto Surface en la ventana de juego en la posición [0, 0]
    dis.blit(value, [0, 0])
 
 
#Esta función dibuja la serpiente en la ventana de juego 
def our_snake(snake_block, snake_list):
#Iteramos a través de cada bloque de la serpiente en la lista snake_list
    for x in snake_list:
#Dibujamos un rectángulo negro en la posición correspondiente al bloque de la serpiente
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
#Esta función muestra un mensaje en pantalla
def message(msg, color):
#Creamos un objeto Surface con el mensaje y el color especificados
    mesg = font_style.render(msg, True, color)
#Dibujamos el objeto Surface en la ventana de juego en la posición [dis_width / 6, dis_height / 3]
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#Esta función es la que controla el ciclo principal del juego 
def gameLoop():

# game_over es una variable booleana que indica si el juego ha terminado o no
    game_over = False

# game_close es una variable booleana que indica si la serpiente ha chocado contra sí misma o no
    game_close = False

# Inicializamos las coordenadas de la cabeza de la serpiente en el centro de la ventana de juego 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
# Inicializamos los cambios en las coordenadas de la cabeza de la serpiente en 0 
    x1_change = 0
    y1_change = 0
 
#Inicializamos una lista vacía que contendrá los bloques de la serpiente 
    snake_List = []

#Inicializamos la longitud de la serpiente en 1 bloque    
    Length_of_snake = 1

#Generamos coordenadas aleatorias para la posición inicial de la comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 

#Este bucle se ejecuta mientras el juego no haya terminado
    while not game_over:

#Este bucle se ejecuta mientras la serpiente haya chocado contra sí misma
        while game_close == True:
#Dibujamos un fondo azul en la ventana de juego
            dis.fill(blue)
#Mostramos un mensaje en pantalla indicando que el jugador ha perdido
            message("Perdiste! Presiona C Para jugar de nuevo o Q para salir", red)
#Mostramos la puntuación del jugador
            Your_score(Length_of_snake - 1)
#Actualizamos la ventana de juego
            pygame.display.update()
 
#Iteramos a través de los eventos de pygame 
            for event in pygame.event.get():
#Si se presiona una tecla
                if event.type == pygame.KEYDOWN:
#Si la tecla presionada es 'q', salimos del juego
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
#Si la tecla presionada es 'c', iniciamos un nuevo juego
                    if event.key == pygame.K_c:
                        gameLoop()
#Iteramos a través de los eventos de pygame
        for event in pygame.event.get():
#Si el evento es cerrar la ventana de juego, se termina el juego
            if event.type == pygame.QUIT:
                game_over = True
#Si el evento es presionar una tecla
            if event.type == pygame.KEYDOWN:
# Si la tecla presionada es la flecha izquierda, cambiamos la dirección a la izquierda
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
#Sino si la tecla presionada es la flecha derecha, cambiamos la dirección a la derecha
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
#Sino si la tecla presionada es la flecha arriba, cambiamos la dirección hacia arriba
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0

#Sino si la tecla presionada es la flecha abajo, cambiamos la dirección hacia abajo
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

#Si la cabeza de la serpiente se sale del borde de la pantalla, el juego se acaba.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

#Cambiamos la posición de la cabeza de la serpiente de acuerdo a su dirección.
        x1 += x1_change
        y1 += y1_change

#Llenamos el fondo de la pantalla con un color azul.     
        dis.fill(blue)

#Dibujamos la comida de la serpiente en una posición aleatoria.
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

#Creamos una lista que contenga las coordenadas de la cabeza de la serpiente.
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

#Agregamos la lista de la cabeza de la serpiente a la lista de la serpiente.      
        snake_List.append(snake_Head)

#Si la longitud de la serpiente es mayor que su tamaño, eliminamos el primer elemento de la lista de la serpiente.
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

# Este bucle itera a través de cada segmento del cuerpo de la serpiente
        for x in snake_List[:-1]:

#Si la posición actual coincide con la posición de la cabeza de la serpiente, se cierra el juego
            if x == snake_Head:
                game_close = True

# Dibuja la serpiente en la pantalla con la longitud y el tamaño del bloque dados
        our_snake(snake_block, snake_List)

# Muestra la puntuación del jugador en la pantalla
        Your_score(Length_of_snake - 1)

#Actualiza la pantalla para mostrar los cambios
        pygame.display.update()
 
# Comprueba si la serpiente ha alcanzado la comida
        if x1 == foodx and y1 == foody:

 # Si la serpiente ha alcanzado la comida, se genera una nueva posición aleatoria para la comida
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# La longitud de la serpiente aumenta en 1 cuando come
            Length_of_snake += 1

# Espera un número específico de milisegundos para controlar la velocidad de la serpiente
        clock.tick(snake_speed)
 
# Cierra el juego de Pygame
    pygame.quit()

# Sale del script de Python
    quit()
 
# Llama a la función gameLoop() para volver a iniciar el juego
gameLoop()