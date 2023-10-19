import pygame
import random
import sys
import time

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Carrera de Atletismo en Pygame")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)

# Fuente para la alerta
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)

runner1_image = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Jamaica.svg.png")
runner1_image = pygame.transform.scale(runner1_image, (15, 15))

# Clase para representar a un corredor
class Runner1:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3 # Velocidad aleatoria

    def move(self):
        self.rect.x += self.speed

# Crea 8 corredores


runners1 = [Runner1(runner1_image, 0 , 20 )]
runners2 = [Runner1(runner1_image, 200 , 20)]
runners3 = [Runner1(runner1_image, 400 , 20)]
runners4 = [Runner1(runner1_image, 600 , 20)]



   
# Bucle principal
running = True
winner = None
game_started = True  # Iniciamos el juego automáticamente

clock = pygame.time.Clock()

while running:
    x = False
    y = False
    z = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(10)
            running = False

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners1:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners2:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners3:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners4:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                winner = runner

    # Limpia la pantalla
    screen.fill(white)

    # Dibuja a los corredores
    for runner in runners1:
        screen.blit(runner.image, runner.rect)
    for runner in runners2:
        screen.blit(runner.image, runner.rect)
    for runner in runners3:
        screen.blit(runner.image, runner.rect)
    for runner in runners4:
        screen.blit(runner.image, runner.rect)

    # Si hay un ganador, muestra una alerta
    if winner:
        alert_text = font.render(f"Ganador: Corredor {runners1.index(winner) + 1}", True, text_color)
        alert_rect = alert_text.get_rect(center=(width // 2, height // 2))
        screen.blit(alert_text, alert_rect)

    # Actualiza la pantalla
    pygame.display.flip()

    clock.tick(60)  # Controla la velocidad de actualización a 60 FPS

    # Si hay un ganador, detén el juego
    if winner:
        running = False

# Cierra Pygame
pygame.quit()
sys.exit()





