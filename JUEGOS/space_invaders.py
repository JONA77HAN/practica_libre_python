import pygame
import random

pygame.init()

# Configuración del juego
ancho = 800
alto = 600
velocidad_nave = 5
velocidad_disparo = 10
enemigo_velocidad = 3

# Colores
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Inicialización de la ventana del juego
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Space Invaders")

reloj = pygame.time.Clock()

# Función principal del juego
def juego_space_invaders():
    jugador = pygame.Rect(ancho // 2 - 25, alto - 50, 50, 50)
    disparos = []
    enemigos = [pygame.Rect(random.randint(0, ancho - 50), random.randint(50, alto // 2), 50, 50) for _ in range(5)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidad_nave
        if teclas[pygame.K_RIGHT] and jugador.right < ancho:
            jugador.x += velocidad_nave

        # Movimiento de los enemigos
        for enemigo in enemigos:
            enemigo.y += enemigo_velocidad
            if enemigo.bottom > alto:
                enemigo.y = random.randint(50, alto // 2)
                enemigo.x = random.randint(0, ancho - 50)

        # Disparos
        for disparo in disparos:
            disparo.y -= velocidad_disparo
            if disparo.y < 0:
                disparos.remove(disparo)

        # Colisiones
        for enemigo in enemigos:
            for disparo in disparos:
                if enemigo.colliderect(disparo):
                    enemigos.remove(enemigo)
                    disparos.remove(disparo)

        # Dibujar en la ventana
        ventana.fill(blanco)
        pygame.draw.rect(ventana, verde, jugador)

        for enemigo in enemigos:
            pygame.draw.rect(ventana, rojo, enemigo)

        for disparo in disparos:
            pygame.draw.rect(ventana, verde, disparo)

        pygame.display.update()
        reloj.tick(30)

if __name__ == "__main__":
    juego_space_invaders()
