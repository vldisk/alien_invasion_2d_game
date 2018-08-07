import json

class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Рекорд не должен сбрасываться.
        self.high_score = self.get_stored_high_score()
        
        # Игра запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        # Счет
        self.score = 0
        # Уровень игры
        self.level = 1
    
    def get_stored_high_score(self):
        filename = 'high_score.json'
        try:
            with open(filename) as f_obj:
                high_score = json.load(f_obj)
        except FileNotFoundError:
            high_score = 0
            
        return high_score
    
    def high_score_writer(self):
        filename = 'high_score.json'
        with open(filename, 'w') as f_obj:
            json.dump(self.high_score, f_obj)
