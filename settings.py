class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233, 233, 233)
        self.ship_limit = 3
        self.ship_speed = 1.9
        self.bullet_speed = 1.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
        self.alien_speed = 3.0
        self.fleet_drop_speed = 4
        self.fleet_direction = 1
        self.sound_channels = 2
        self.font_size = 15
        self.layoutY = 100
        self.layoutX = self.screen_width - 125
        self.table_width = 100
        self.table_height = 50
        self.table_button_color = (233, 233, 233)
        self.table_text_color = (0, 0, 0)
        self.table_font_size = 48


if __name__ == '__main__':
    print("Settings started in this window")
