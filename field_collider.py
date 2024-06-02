import pygame
from pygame.sprite import Sprite


class FieldCollider(Sprite):
    def __init__(self, game, position, field):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.field = field

        self.image = pygame.image.load('images/field_collider.bmp')

        self.rect = self.image.get_rect()

        self.rect.topleft = position

    def update(self):
        self.screen.blit(self.image, self.rect)
