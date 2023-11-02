import pygame, controls
import sys
from main_character import MainCharacter
from pygame.sprite import Group


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("mordovina")

    maincharacter = MainCharacter(screen)
    enemys = Group()
    bullets = Group()
    controls.create_army(screen, enemys)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.rect.centerx += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    maincharacter.move_right = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    maincharacter.move_right -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    maincharacter.move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    maincharacter.move_left = False


        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        screen.fill(0)
        for bullet in bullets.sprites():
            bullet.draw_bullet()


        controls.update(screen, enemys, maincharacter, bullets)
        controls.update_bullets(screen, enemys, bullets)



        maincharacter.output()
        pygame.display.flip()

        bullets.update()
        for bullet



