import pygame
import time
import random

pygame.init()

# Configuración del juego
ancho = 800
alto = 600
tamaño_celda = 20
velocidad = 15

# Colores
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Inicialización de la ventana del juego
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

reloj = pygame.time.Clock()

# Función principal del juego
def juego_snake():
    juego_terminado = False
    game_over_font = pygame.font.SysFont(None, 55)
    
    # Inicialización de la serpiente
    serpiente = [{"x": ancho / 2, "y": alto / 2}]
    longitud_serpiente = 1

    # Inicialización de la comida
    comida = {"x": round(random.randrange(0, ancho - tamaño_celda) / 10.0) * 10.0,
              "y": round(random.randrange(0, alto - tamaño_celda) / 10.0) * 10.0}

    # Dirección inicial de la serpiente
    dirección = "DERECHA"
    cambio_dirección = dirección

    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not dirección == "DERECHA":
                    cambio_dirección = "IZQUIERDA"
                elif evento.key == pygame.K_RIGHT and not dirección == "IZQUIERDA":
                    cambio_dirección = "DERECHA"
                elif evento.key == pygame.K_UP and not dirección == "ABAJO":
                    cambio_dirección = "ARRIBA"
                elif evento.key == pygame.K_DOWN and not dirección == "ARRIBA":
                    cambio_dirección = "ABAJO"

        # Actualización de la dirección de la serpiente
        dirección = cambio_dirección

        # Movimiento de la serpiente
        if dirección == "IZQUIERDA":
            serpiente[0]["x"] -= tamaño_celda
        elif dirección == "DERECHA":
            serpiente[0]["x"] += tamaño_celda
        elif dirección == "ARRIBA":
            serpiente[0]["y"] -= tamaño_celda
        elif dirección == "ABAJO":
            serpiente[0]["y"] += tamaño_celda

        # Colisión con los bordes
        if (serpiente[0]["x"] >= ancho or serpiente[0]["x"] < 0 or
            serpiente[0]["y"] >= alto or serpiente[0]["y"] < 0):
            juego_terminado = True

        # Colisión con la comida
        if (serpiente[0]["x"] == comida["x"] and serpiente[0]["y"] == comida["y"]):
            comida = {"x": round(random.randrange(0, ancho - tamaño_celda) / 10.0) * 10.0,
                      "y": round(random.randrange(0, alto - tamaño_celda) / 10.0) * 10.0}
            longitud_serpiente += 1

        # Dibujar la serpiente y la comida en la ventana
        ventana.fill(blanco)
        for segmento in serpiente:
            pygame.draw.rect(ventana, verde, [segmento["x"], segmento["y"], tamaño_celda, tamaño_celda])

        pygame.draw.rect(ventana, rojo, [comida["x"], comida["y"], tamaño_celda, tamaño_celda])

        pygame.display.update()

        # Control de la velocidad del juego
        reloj.tick(velocidad)

    # Mostrar mensaje de Game Over
    mensaje = game_over_font.render("Game Over", True, rojo)
    ventana.blit(mensaje, [ancho / 4, alto / 2])
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

if __name__ == "__main__":
    juego_snake()
