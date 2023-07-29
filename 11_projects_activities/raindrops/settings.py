class Settings:
    """A class to store all settings for Raindrop game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Set the background color.
        self.bg_color = (230, 230, 230)

        # Raindrop settings
        self.raindrop_speed = 1.5
