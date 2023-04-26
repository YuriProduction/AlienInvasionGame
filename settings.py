class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233, 233, 233)
        # Ship
        self.ship_limit = 3
        # ___bullet_settings_____________
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
        # Alien
        self.alien_speed = 3.0
        self.fleet_drop_speed = 7  # Величина снижения
        self.fleet_direction = 1
        self.sound_channels = 2


if __name__ == '__main__':
    print("Settings started in this window")
