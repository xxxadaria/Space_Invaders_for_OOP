import pygame
import sys
from hero import MainCharacter

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("mordovina")
    maincharacter = MainCharacter(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    maincharacter.move_right = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.move_right = True



        maincharacter.output()
        pygame.display.flip()


start_game()