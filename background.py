
import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    """Класс, представляет бэкграунд"""
    
    def __init__(self, ai_settings, screen):
        super(Background, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.bg_image = pygame.image.load('images/star_fon.jpg')
        self.bg_rect = self.bg_image.get_rect()
    
    
    def blitme(self):
        """Выводит бэкграунд."""
        self.screen.blit(self.bg_image, self.bg_rect)
