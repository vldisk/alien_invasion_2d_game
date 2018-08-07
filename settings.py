
import pygame


class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        
        # Параметры экрана
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (0, 0, 0)
        
        # Настройки корабля
        self.ship_limit = 3
        
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 243, 10, 243
        self.bullets_allowed = 5 # Колчество разрешенных пуль на экране
        
        # Настройки пришельцев
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.3
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        # Настройки корабля
        self.ship_speed_factor = 10
        
        # Параметры пули
        self.bullet_speed_factor = 10
        
        # Настройки пришельцев
        self.alien_speed_factor = 5
        
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        
        # Подсчет очков
        self.alien_points = 50
    
    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

