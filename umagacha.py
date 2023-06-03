import pygame
import random
import math
import os

class Horse:
    def __init__(self, name, image_path):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

pygame.init()
pygame.mixer.init()

X = 1024
Y = 668
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Umagatcha')

icon_image = pygame.image.load("logo.ico")
pygame.display.set_icon(icon_image)
background = pygame.image.load('background.png')

horses = [
    Horse("Character b0", "standartbred_black_mare_bob.png"),
    Horse("Character b1", "standartbred_black_mare_braids.png"),
    Horse("Character b2", "standartbred_black_mare_bubbly.png"),
    Horse("Character b3", "standartbred_black_mare_curls.png"),
    Horse("Character b4", "standartbred_black_mare_sideswept.png"),
    Horse("Character b5", "standartbred_black_stallion_bob.png"),
    Horse("Character b6", "standartbred_black_stallion_braids.png"),
    Horse("Character b7", "standartbred_black_stallion_bubbly.png"),
    Horse("Character b8", "standartbred_black_stallion_curls.png"),
    Horse("Character b9", "standartbred_black_stallion_sideswept.png"),
]

# Set up game states
class Game:
    MENU = 0
    CHOOSE_THE_CHARACTER = 1
    MAIN = 2
    FOOD = 3
    WATER = 4
    BRUSH = 5
    HOOFPICK = 6
    BACKGROUND = 7
    DRESSAGE = 8
    SHOWJUMPIN = 9
    MAP = 10
    END = 11

current_state = Game.MENU

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    if current_state == Game.MENU:
        tamago = pygame.image.load('tamago.png')
        screen.blit(tamago, (0, 0))
        scrn = pygame.image.load('screen.png')
        screen.blit(scrn, (0, 0))
        decor_buttons = pygame.image.load('buttons.png')
        screen.blit(decor_buttons, (0, 0))
        start_the_game = pygame.image.load('start.png')
        screen.blit(start_the_game, (0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            track1 = pygame.mixer.Sound("aud-20150922-wa0001.mp3")
            track1.play()
            if mouse_presses[0]:
                pygame.time.wait(3000)
                current_state = Game.CHOOSE_THE_CHARACTER

    elif current_state == Game.CHOOSE_THE_CHARACTER:

        tamago = pygame.image.load('tamago.png')
        screen.blit(tamago, (0, 0))
        scrnbase = pygame.image.load('screen_base.png')
        screen.blit(scrnbase, (0, 0))
        decor_buttons = pygame.image.load('buttons.png')
        screen.blit(decor_buttons, (0, 0))
        choose = pygame.image.load('click_to_choose.png')
        screen.blit(choose, (0, 0))
        begin = pygame.image.load('begin.png')
        screen.blit(begin, (0, 0))
        random_horse = random.choice(horses)
        screen.blit(random_horse.image, (X/2.5, Y/3))

        horse_generated = False
        last_generated_horse = None

        while not horse_generated:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        random_horse = random.choice(horses)
                        last_generated_horse = random_horse
                        horse_generated = True
                        break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        horse_generated = True
                        current_state = Game.MAIN
                        break

    elif current_state == Game.MAIN:
        herd = []
        horse0 = None

        tamago = pygame.image.load('tamago.png')
        screen.blit(tamago, (0, 0))
        stable_back = pygame.image.load('stable_back.png')
        screen.blit(stable_back, (0, 0))
        decor_buttons = pygame.image.load('buttons.png')
        screen.blit(decor_buttons, (0, 0))

        if random_horse == horses[0]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_mare_bob.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[1]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_mare_braids.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[2]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_mare_bubbly.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[3]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_mare_curls.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[4]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_mare_sideswept.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[5]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_stallion_bob.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[6]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_stallion_braids.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[7]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_stallion_bubbly.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[8]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_stallion_curls.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))
        elif random_horse == horses[9]:
            herd.append(random_horse)
            horse0 = pygame.image.load('standartbred_black_stallion_sideswept.png')
            screen.blit(horse0, (X / 2.5, Y / 3.25))

        stable_front = pygame.image.load('stable_front.png')
        screen.blit(stable_front, (0, 0))
        lowerbox = pygame.image.load('lowebox.png')
        screen.blit(lowerbox, (0, 0))

        food = pygame.image.load('food.png')
        button_rect = button_image.get_rect()
        button_rect.x = (1024-390)
        button_rect.y = (668-464)
        water = pygame.image.load('water.png')
        screen.blit(water, (420, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        brush = pygame.image.load('brush.png')
        screen.blit(brush, (450, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        hoofpick = pygame.image.load('hoofpick.png')
        screen.blit(hoofpick, (480, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        halter = pygame.image.load('halter.png')
        screen.blit(halter, (510, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        dressage = pygame.image.load('dressage.png')
        screen.blit(dressage, (540, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        showjumping = pygame.image.load('showjumping.png')
        screen.blit(showjumping, (570, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2
        map = pygame.image.load('map.png')
        screen.blit(map, (600, 464))
        button_rect = button_image.get_rect()
        button_rect.x = (screen_width - button_width) // 2
        button_rect.y = (screen_height - button_height) // 2

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 5:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 6:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 7:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 8:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 9:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")

    pygame.display.flip()

pygame.display.flip()
clock.tick(60)
pygame.quit()