import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,50,50)
        self.color = 255,0,0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_enemy(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def moving_enemy(self):
        self.y += 0.5
        self.rect.y = self.y