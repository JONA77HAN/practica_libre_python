import pygame
import sys

pygame.init()

# Configuración del juego
ancho = 800
alto = 600
velocidad = 5

# Colores
blanco = (255, 255, 255)

# Inicialización de la ventana del juego
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pong")

reloj = pygame.time.Clock()

# Inicialización de las paletas y la pelota
paleta_izquierda = pygame.Rect(50, alto // 2 - 50, 20, 100)
paleta_derecha = pygame.Rect(ancho - 70, alto // 2 - 50, 20, 100)
pelota = pygame.Rect(ancho // 2 - 15, alto // 2 - 15, 30, 30)

direccion_pelota = [1, 1]  # Dirección inicial de la pelota (derecha y abajo)

# Función principal del juego
def juego_pong():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento de las paletas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and paleta_izquierda.top > 0:
            paleta_izquierda.y -= velocidad
        if teclas[pygame.K_s] and paleta_izquierda.bottom < alto:
            paleta_izquierda.y += velocidad
        if teclas[pygame.K_UP] and paleta_derecha.top > 0:
            paleta_derecha.y -= velocidad
        if teclas[pygame.K_DOWN] and paleta_derecha.bottom < alto:
            paleta_derecha.y += velocidad

        # Movimiento de la pelota
        pelota.x += direccion_pelota[0] * velocidad
        pelota.y += direccion_pelota[1] * velocidad

        # Colisiones con las paletas
        if pelota.colliderect(paleta_izquierda) or pelota.colliderect(paleta_derecha):
            direccion_pelota[0] *= -1

        # Colisiones con los bordes
        if pelota.top <= 0 or pelota.bottom >= alto:
            direccion_pelota[1] *= -1

        # Reiniciar la posición de la pelota si sale por los lados
        if pelota.left <= 0 or pelota.right >= ancho:
            pelota.x = ancho // 2 - 15
            pelota.y = alto // 2 - 15

        # Dibujar en la ventana
        ventana.fill(blanco)
        pygame.draw.rect(ventana, blanco, paleta_izquierda)
        pygame.draw.rect(ventana, blanco, paleta_derecha)
        pygame.draw.ellipse(ventana, blanco, pelota)

        pygame.display.update()
        reloj.tick(60)

if __name__ == "__main__":
    juego_pong()
