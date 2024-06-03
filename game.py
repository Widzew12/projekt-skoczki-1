import sys

import pygame

from static_variables import *

from game_board import GameBoard
from settings import Settings
from button import Button
from game_board_display import GameBoardDisplay
from field_colliders import FieldColliders
from move import Move
from information_text import InformationText
from turn_display import TurnDisplay


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.game_board = GameBoard()

        self.starting_field = None
        self.target_field = None
        self.current_turn = WHITE

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Skoczki")

        self._initialize_background()

        self.game_board_display = GameBoardDisplay(self)
        self.field_colliders = FieldColliders(self)

        self.information_text = InformationText(self)
        self.information_text.change_text("Click starting field.")

        self.turn_display = TurnDisplay(self)
        self.turn_display.update_turn_display()

        # Start the game in an inactive state.
        self.game_active = False

        self._make_play_button()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                pass

            self._update_screen()
            self.clock.tick(60)

    def _make_play_button(self):
        self.play_button_rect = pygame.Rect(0, 0, 200, 50)
        self.play_button_rect.center = self.screen.get_rect().center
        self.play_button_color = (0, 135, 0)
        self.play_button_text_color = (255, 255, 255)
        self.play_button = Button(self, "Play", self.play_button_rect, self.play_button_color,
                                  self.play_button_text_color)

    def _initialize_background(self):
        self.background_image = pygame.image.load('images/game_board.bmp')
        self.background_image_rect = self.background_image.get_rect()
        self.background_image_rect.topleft = (0, 0)

    def _update_background(self):
        self.screen.blit(self.background_image, self.background_image_rect)

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
            self._check_field_colliders(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player click Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._use_play_button()

    def _check_field_colliders(self, mouse_pos):
        field_colliders = self.field_colliders.field_colliders
        for field_collider in field_colliders:
            if field_collider.rect.collidepoint(mouse_pos):
                clicked_field = field_collider.field
                if self.game_active:
                    self._use_field(clicked_field)

    def _use_field(self, field):
        if self.starting_field is None:
            self.starting_field = field
            if field.content != self.current_turn:
                self._reset_starting_and_target_fields()
                return
            self.information_text.change_text("Click target field.")
        elif self.target_field is None:
            self.target_field = field
            move = Move(self.starting_field, self.target_field, self.game_board)
            self._try_make_move(move)
            self.information_text.change_text("Click starting field.")

    def _try_make_move(self, move):
        if move.check_and_make_move():
            new_board_tuple = move.new_board_tuple
            self.game_board.change_board(new_board_tuple)
            self._change_turn()
            self.game_board_display.update_board_display()
            self.field_colliders.update_board()
            self.turn_display.update_turn_display()

        self._reset_starting_and_target_fields()

    def _reset_starting_and_target_fields(self):
        self.starting_field = None
        self.target_field = None

    def _use_play_button(self):
        self.game_active = True

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _change_turn(self):
        if self.current_turn == WHITE:
            self.current_turn = BLACK
        elif self.current_turn == BLACK:
            self.current_turn = WHITE

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self._update_background()

        self.game_board_display.update_screen()
        self.field_colliders.update_screen()
        self.information_text.update_screen()
        self.turn_display.update_screen()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def print_board(self):
        print("-----------------------------------------------------------------")
        for row in self.game_board.current_game_board_tuple:
            output_row = "| "
            for field_content in row:
                output_row += field_content + " | "
            print(output_row)
            print("-----------------------------------------------------------------")


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
