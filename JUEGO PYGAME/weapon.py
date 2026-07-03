
import pygame
import constantes
import math



class Weapon():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()


    def update(self, personaje):
        bala = None
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/4
            self.rotar_arma(True)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width/4
            self.rotar_arma(False)


       #mover el arma con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        #print(self.angulo)
        #detectar  los clicks del mouse
        if pygame.mouse.get_pressed()[0]:
            bala = Bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
        return bala



    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_ARMA, self.forma, 1)




class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x , y , angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def dibujar(self, intefaz):
        intefaz.blit(self.image, (self.rect.centerx,
                     self.rect.centery - int(self.image.get_height()/2)))
