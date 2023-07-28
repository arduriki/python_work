import pygame


class Jedi:
    """A class to manage a Jedi."""

    def __init__(self, bs_game):
        """Initialize the Jedi and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the Jedi image and get its rect.
        self.image = pygame.image.load('images/yoda.bmp')
        self.rect = self.image.get_rect()

        # Start each new Jedi at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the Jedi at its current location."""
        self.screen.blit(self.image, self.rect)