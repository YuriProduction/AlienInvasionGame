from settings import Settings


# pragma : no cover
class GameStats:
    # pragma : no cover
    def __init__(self):
        self.settings = Settings()
        self.ships_count = self.settings.ship_limit
        self.game_active = True
