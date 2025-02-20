import pygame

#инициализация мейн героя
class MainCharacter():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/main_character.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def moving(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= 1
            
            
    def create_hero_again(self):
        self.center = self.screen_rect.centerx

        

