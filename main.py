import pygame, controls
import sys
from main_character import MainCharacter
from pygame.sprite import Group

#основная функ ДЛЯ ОПИСАНИЯ игры
def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("mordovina")
    

#объекты классов
    maincharacter = MainCharacter(screen)
    bullets = Group()
    enemys = Group()
    controls.create_army(screen,enemys)

    flag = True
    while flag:
        controls.events(screen, hero, bullets)
        hero.moving_hero(screen)

        controls.update(screen, hero, enemys, bullets)
        controls.update_bullets(screen, bullets, enemys)
        controls.update_enemys(hero,screen, bullets, enemys)
        

start_game()

        



