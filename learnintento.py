import pygame
import random
import sys
import time

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
width, height = 838, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Carrera de Atletismo en Pygame")

# Colores
white = (245, 235, 225)
red = (255, 0, 0)

# Fuente para la alerta
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)



estadosunidos = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/172959-flag-usa-png-free-photo.png")
estadosunidos = pygame.transform.scale(estadosunidos, (20, 20))

francia = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_France.svg.png")
francia = pygame.transform.scale(francia,(20,20))

jamaica = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Jamaica.svg.png")
jamaica = pygame.transform.scale(jamaica, (20, 20))

etiopia = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Ethiopia_(1897–1974).svg.png")
etiopia = pygame.transform.scale(etiopia, (20, 20))

polonia = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Poland.svg.png")
polonia = pygame.transform.scale(polonia, (20, 20))

Holanda = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_the_Netherlands.svg.webp")
Holanda = pygame.transform.scale(Holanda,(20,20))

belgica = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/Flag_of_Belgium.svg.png")
belgica = pygame.transform.scale(belgica, (20, 20))

kenia = pygame.image.load("/Users/mateovera/Documents/Programación/Python_intermediate/discretas/kENIA.png")
kenia = pygame.transform.scale(kenia, (20, 20))

#Velocidad
velocidad = 20

#Clase Numero1
class Runner1:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = (velocidad * 0.20) # Velocidad aleatoria

    def move(self):
        self.rect.x += self.speed

#Clase Numero2
class Runner2:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = (velocidad * 0.05) # Velocidad aleatoria

    def move(self):
        self.rect.x += self.speed

#Clase Numero3

class Runner3:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = (velocidad * 0.15) # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero4

class Runner4:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = (velocidad * 0.18) # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero5

class Runner5:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = (velocidad * 0.13) # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero6

class Runner6:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = (velocidad * 0.10) # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero7

class Runner7:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = (velocidad * 0.07) # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed

#Clase Numero8

class Runner8:
        def __init__(self, image, x, y):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = velocidad * 0.12 # Velocidad aleatoria

        def move(self):
            self.rect.x += self.speed


#Corredores1
runners1 = [Runner1(estadosunidos, 0 , 40 )]
runners2 = [Runner1(estadosunidos, 200 , 40)]
runners3 = [Runner1(estadosunidos, 400 , 40)]
runners4 = [Runner1(estadosunidos, 600 ,40)]

#Corredores2
runners5 = [Runner2(francia, 0 , 80 )]
runners6 = [Runner2(francia, 200 , 80)]
runners7 = [Runner2(francia, 400 , 80)]
runners8 = [Runner2(francia, 600 , 80)]

#Corredores3
runners9 = [Runner3(jamaica, 0 , 120 )]
runners10 = [Runner3(jamaica, 200 , 120)]
runners11 = [Runner3(jamaica, 400 , 120)]
runners12 = [Runner3(jamaica, 600 , 120)]

#Corredores4

runners13 = [Runner4(etiopia, 0 , 160 )]
runners14 = [Runner4(etiopia, 200 , 160)]
runners15 = [Runner4(etiopia, 400 , 160)]
runners16 = [Runner4(etiopia, 600 , 160)]

#Corredores5

runners17 = [Runner5(polonia, 0 , 200 )]
runners18 = [Runner5(polonia, 200 , 200)]
runners19 = [Runner5(polonia, 400 , 200)]
runners20 = [Runner5(polonia, 600 , 200)]

#Corredores6

runners21 = [Runner6(Holanda, 0 , 240 )]
runners22 = [Runner6(Holanda, 200 , 240)]
runners23 = [Runner6(Holanda, 400 , 240)]
runners24 = [Runner6(Holanda, 600 , 240)]

#Corredores7

runners25 = [Runner7(belgica, 0 , 280 )]
runners26 = [Runner7(belgica, 200 , 280)]
runners27 = [Runner7(belgica, 400 , 280)]
runners28 = [Runner7(belgica, 600 , 280)]

#Corredores8

runners29 = [Runner8(kenia, 0 , 320 )]
runners30 = [Runner8(kenia, 200 , 320)]
runners31 = [Runner8(kenia, 400 ,320)]
runners32 = [Runner8(kenia, 600 , 320)]


# Bucle principal
running = True
winner = None
game_started = True  # Iniciamos el juego automáticamente
ganador = False

clock = pygame.time.Clock()


while running:
    

    x = False
    y = False
    z = False
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
                runner.speed = 0

                #Oro Plata Y Bronce
                oro = "Estados unidos"
                plata = " Etiopía"
                bronce = "Jamaica"
                text = font.render(f' Oro para {oro}   Plata para {plata}   Bronce {bronce}', True, text_color)
                
                ganador = True


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
                winner = runner
                ganador = True

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
 
         #       paisganador = "Jamaica"
        #        text = font.render(f'El ganador es {paisganador}', True, text_color)
                ganador = True



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
                ganador = True

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
                ganador = True

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
                ganador = True


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
                ganador = True

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
                ganador = True

                


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


    # Si hay un ganador, muestra una alerta
    if ganador:
        screen.blit(text, (70, 410))

    text_surface = font.render("400m", True, text_color)
    screen.blit(text_surface, (163, 350))

    text_surface = font.render("800m", True, text_color)
    screen.blit(text_surface, (363, 350))

    text_surface = font.render("1200m", True, text_color)
    screen.blit(text_surface, (563, 350))

    text_surface = font.render("1600m", True, text_color)
    screen.blit(text_surface, (760, 350))

    # Actualiza la pantalla
    pygame.display.flip()

    clock.tick(60)  # Controla la velocidad de actualización a 60 FPS

    # Si hay un ganador, detén el juego
   
    if winner:
        time.sleep(10)
        running = False

# Cierra Pygame
pygame.quit()
sys.exit()