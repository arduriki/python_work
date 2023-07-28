import sys

import pygame

from jedi import Jedi

class BlueSky:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        self.jedi = Jedi(self)

        # Set the background color.
        self.bg_color = (2, 51, 43)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.jedi.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()