
import pygame
from pygame.sprite import Group

from settings import Settings
from background import Background
from ship import Ship

import game_functions as gf

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
                        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Создание бэкграунда.
    background = Background(ai_settings, screen)
    
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    
    # Создание группы для хранения пуль.
    bullets = Group()
    
    # Создание группы для хранения пришельцев
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
                            aliens, bullets)
        
        if stats.game_active:
            # Позиция корабля обновляется в ответ на действия пользователя
            ship.update()
            # Обновляет позиции пуль и уничтожает старые пули.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                                    aliens, bullets)
            # Обновляет позиции пришельцев
            gf.update_aliens(ai_settings, screen, stats, sb, ship, 
                                    aliens, bullets)
        
        # Обновляет изображения на экране и отображает новый экран.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
                                bullets, play_button, background)

run_game()
