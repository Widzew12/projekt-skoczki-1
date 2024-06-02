import sys

import pygame

from static_values import *

from settings import Settings
from button import Button


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Skoczki")

        # Start the game in an inactive state.
        self.game_active = False

        self._make_play_button()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                print(self.game_active)

            self._update_screen()
            self.clock.tick(60)

    def _make_play_button(self):
        self.play_button_rect = pygame.Rect(0, 0, 200, 50)
        self.play_button_rect.center = self.screen.get_rect().center
        self.play_button_color = (0, 135, 0)
        self.play_button_text_color = (255, 255, 255)
        self.play_button = Button(self, "Play", self.play_button_rect, self.play_button_color, self.play_button_text_color)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events(event)

    def _check_mouse_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.button == pygame.BUTTON_LEFT:
            self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player click Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._use_pause_button()

    def _use_pause_button(self):
        self.game_active = True

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
