import pygame
import random
import sys
import time

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Carrera de Atletismo en Pygame")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)

# Fuente para la alerta
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)

runner1_image = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Jamaica.svg.png")
runner1_image = pygame.transform.scale(runner1_image, (20, 20))

#Clase Numero1
class Runner1:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1 # Velocidad aleatoria

    def move(self):
        self.rect.x += self.speed

#Clase Numero2
class Runner2:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2 # Velocidad aleatoria

    def move(self):
        self.rect.x += self.speed

#Clase Numero3

class Runner3:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 3 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero4

class Runner4:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 2.5 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero5

class Runner5:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 4 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero6

class Runner6:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 3 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero7

class Runner7:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 2 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero8

class Runner8:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 1 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed


#Corredores1
runners1 = [Runner1(runner1_image, 0 , 40 )]
runners2 = [Runner1(runner1_image, 200 , 40)]
runners3 = [Runner1(runner1_image, 400 , 40)]
runners4 = [Runner1(runner1_image, 600 ,40)]

#Corredores2
runners5 = [Runner2(runner1_image, 0 , 80 )]
runners6 = [Runner2(runner1_image, 200 , 80)]
runners7 = [Runner2(runner1_image, 400 , 80)]
runners8 = [Runner2(runner1_image, 600 , 80)]

#Corredores3
runners9 = [Runner3(runner1_image, 0 , 120 )]
runners10 = [Runner3(runner1_image, 200 , 120)]
runners11 = [Runner3(runner1_image, 400 , 120)]
runners12 = [Runner3(runner1_image, 600 , 120)]

#Corredores4

runners13 = [Runner4(runner1_image, 0 , 160 )]
runners14 = [Runner4(runner1_image, 200 , 160)]
runners15 = [Runner4(runner1_image, 400 , 160)]
runners16 = [Runner4(runner1_image, 600 , 160)]

#Corredores5

runners17 = [Runner5(runner1_image, 0 , 200 )]
runners18 = [Runner5(runner1_image, 200 , 200)]
runners19 = [Runner5(runner1_image, 400 , 200)]
runners20 = [Runner5(runner1_image, 600 , 200)]

#Corredores6

runners21 = [Runner6(runner1_image, 0 , 240 )]
runners22 = [Runner6(runner1_image, 200 , 240)]
runners23 = [Runner6(runner1_image, 400 , 240)]
runners24 = [Runner6(runner1_image, 600 , 240)]

#Corredores7

runners25 = [Runner7(runner1_image, 0 , 280 )]
runners26 = [Runner7(runner1_image, 200 , 280)]
runners27 = [Runner7(runner1_image, 400 , 280)]
runners28 = [Runner7(runner1_image, 600 , 280)]

#Corredores8

runners29 = [Runner8(runner1_image, 0 , 320 )]
runners30 = [Runner8(runner1_image, 200 , 320)]
runners31 = [Runner8(runner1_image, 400 ,320)]
runners32 = [Runner8(runner1_image, 600 , 320)]


# Bucle principal
running = True
winner = None
game_started = True  # Iniciamos el juego automáticamente

clock = pygame.time.Clock()

while running:
    x = False
    y = False
    z = False
    m = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(10)
            running = False

#Corredores Equipo1

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

#Corredores Equipo2

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners5:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
      

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners6:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners7:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners8:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True

#Corredores Equipo3

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners9:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners10:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners11:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners12:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True


#Corredores Equipo4

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners13:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners14:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners15:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners16:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True

#Corredores Equipo5

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners17:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners18:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners19:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners20:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True

#Corredores Equipo6

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners21:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners22:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners23:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners24:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True


#Corredores Equipo7

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners25:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners26:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners27:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners28:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True

#Corredores Equipo8

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        for runner in runners29:
            runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 180
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                x = True
        

    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if x:
            for runner in runners30:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 380
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                y = True
        
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if y:
            for runner in runners31:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 580
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                z = True
                
                
    if game_started:
        # Actualiza la posición de los corredores de manera animada
        if z:
            for runner in runners32:
                
                runner.move()

            # Verifica si un corredor ha llegado a la línea de meta
            finish_line = 780
            if runner.rect.x >= finish_line and winner is None:
                runner.speed = 0
                winner = True
                


# Limpia la pantalla
    screen.fill(white)

# Dibuja a los corredores Equipo1
    for runner in runners1:
        screen.blit(runner.image, runner.rect)
    for runner in runners2:
        screen.blit(runner.image, runner.rect)
    for runner in runners3:
        screen.blit(runner.image, runner.rect)
    for runner in runners4:
        screen.blit(runner.image, runner.rect)

# Dibuja a los corredores Equipo2
    for runner in runners5:
        screen.blit(runner.image, runner.rect)
    for runner in runners6:
        screen.blit(runner.image, runner.rect)
    for runner in runners7:
        screen.blit(runner.image, runner.rect)
    for runner in runners8:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo3
    for runner in runners9:
        screen.blit(runner.image, runner.rect)
    for runner in runners10:
        screen.blit(runner.image, runner.rect)
    for runner in runners11:
        screen.blit(runner.image, runner.rect)
    for runner in runners12:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo4

    for runner in runners13:
        screen.blit(runner.image, runner.rect)
    for runner in runners14:
        screen.blit(runner.image, runner.rect)
    for runner in runners15:
        screen.blit(runner.image, runner.rect)
    for runner in runners16:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo5

    for runner in runners17:
        screen.blit(runner.image, runner.rect)
    for runner in runners18:
        screen.blit(runner.image, runner.rect)
    for runner in runners19:
        screen.blit(runner.image, runner.rect)
    for runner in runners20:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo6

    for runner in runners21:
        screen.blit(runner.image, runner.rect)
    for runner in runners22:
        screen.blit(runner.image, runner.rect)
    for runner in runners23:
        screen.blit(runner.image, runner.rect)
    for runner in runners24:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo7

    for runner in runners25:
        screen.blit(runner.image, runner.rect)
    for runner in runners26:
        screen.blit(runner.image, runner.rect)
    for runner in runners27:
        screen.blit(runner.image, runner.rect)
    for runner in runners28:
        screen.blit(runner.image, runner.rect)

#Dibuja a los corredores Equipo8

    for runner in runners29:
        screen.blit(runner.image, runner.rect)
    for runner in runners30:
        screen.blit(runner.image, runner.rect)
    for runner in runners31:
        screen.blit(runner.image, runner.rect)
    for runner in runners32:
        screen.blit(runner.image, runner.rect)


winner = []
    # Si hay un ganador, muestra una alerta
    if winner:
        alert_text = font.render(f"Ganador: Corredor", True, text_color)
        alert_rect = alert_text.get_rect(center=(width // 2, height // 2))
        screen.blit(alert_text, alert_rect)

    if winners:
        winner_text = font.render(f"Ganador(es):", True, text_color)
        screen.blit(winner_text, (10, 10))
        y = 40
        for winner in winners:
            winner_number = runners.index(winner) + 1
            winner_text = font.render(f"Corredor {winner_number}", True, text_color)
            screen.blit(winner_text, (10, y))
            y += 30


    # Actualiza la pantalla
    pygame.display.flip()

    clock.tick(60)  # Controla la velocidad de actualización a 60 FPS

    # Si hay un ganador, detén el juego


# Cierra Pygame
pygame.quit()
sys.exit()





