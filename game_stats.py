from settings import Settings


class GameStats:
    def __init__(self):
        self.settings = Settings()
        self.ships_count = self.settings.ship_limit
        self.game_active = True

