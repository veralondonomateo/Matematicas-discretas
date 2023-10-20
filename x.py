import pygame
import sys
import time

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Carrera de Atletismo en Pygame")

white = (255, 255, 255)

# Define la velocidad de los corredores
speeds = [1, 2, 3, 2.5, 4, 3, 2, 1]

class Runner:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self):
        self.rect.x += self.speed

# Crea los corredores y agrégalos a una lista
runner_images = [pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Jamaica.svg.png") for _ in range(8)]
runners = [Runner(runner_images[i], 0, 40 + i * 40, speeds[i]) for i in range(8)]

running = True
winner = None
game_started = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_started and winner is None:
        for runner in runners:
            runner.move()
            if runner.rect.x >= width - 20:  # Adjust this value to control the finish line
                winner = runner

    screen.fill(white)

    for runner in runners:
        screen.blit(runner.image, runner.rect)

    pygame.display.flip()

    clock.tick(60)

    if winner:
        running = False

pygame.quit()
sys.exit()
