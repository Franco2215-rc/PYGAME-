import pygame
from pygame.cursors import sizer_x_strings
from pygame.threads import benchmark_workers

import constantes
import personaje
from weapon import Weapon
from personaje import Personaje
from constantes import ALTO_VENTANA, ESCALA_PERSONAJE


pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
pygame.display.set_caption("PAKOVAGAME")

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen


#Importar imagenes
#Personaje
animaciones = []
for i in range(6):
    img = pygame.image.load(f"assets/images/characters/player//Player_{i}.png").convert_alpha()
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)
#Arma
imagen_pistola = pygame.image.load(f"assets//images//weapons//gun.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constantes.ESCALA_ARMA)

#Bala
imagen_balas = pygame.image.load(f"assets//images//weapons//bullet.png").convert_alpha()
imagen_balas = escalar_img(imagen_balas, constantes.ESCALA_ARMA)
imagen_balas = pygame.transform.scale(
    imagen_balas,
    (
        int(imagen_balas.get_width() * constantes.ESCALA_BALA),
        int(imagen_balas.get_height() * constantes.ESCALA_BALA)
    )
)


#crear pj de la clase personaje
jugador = Personaje(50,50, animaciones)
#crear arma de la clase weapon
pistola = Weapon(imagen_pistola, imagen_balas)
#crear un grupo de sprites
grupos_balas = pygame.sprite.Group()





#Definir variables de movimiento
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

    #controlar el frame rate
reloj = pygame.time.Clock()



run = True
while run == True:


    reloj.tick(constantes.FPS)




    ventana.fill(constantes.COLOR_BG)
    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    #Actualizar estado del jugador
    jugador.update()
    #Actualiza el estado del arma
    bala = pistola.update(jugador)
    if bala:
        grupos_balas.add(bala)

    print(grupos_balas)



    #dibujar al jugador
    jugador.dibujar(ventana)

    #dibujar el arma
    pistola.dibujar(ventana)

    #dibujar balas
    for bala in grupos_balas:
        bala.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

              #Se suelta la tecla

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                    mover_izquierda = False
            if event.key == pygame.K_d:
                    mover_derecha = False
            if event.key == pygame.K_w:
                    mover_arriba = False
            if event.key == pygame.K_s:
                    mover_abajo = False

    pygame.display.update()

pygame.quit()