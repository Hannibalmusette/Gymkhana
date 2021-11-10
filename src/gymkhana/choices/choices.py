import pygame
from .inputbox import InputBox
from .write_text import write_text
from gymkhana.player import Player
from gymkhana.constants import WIDTH, HEIGHT, WIN, WRITING_COLOR, BG_COLOR

pygame.init()

def make_rect(x, y, w, h):
    return pygame.Rect(x, y, w, h)

def draw_rect(rect, color=WRITING_COLOR, win=WIN):
    pygame.draw.rect(win, color, rect, 2)

def is_ready(event, button) -> bool:
    return event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(
        event.pos
    )

def update_player(player: Player, inputbox: InputBox, event):
    (player.color, player.name, player.bot) = inputbox.handle_event(event)


def choices(win=WIN, bgcolor=BG_COLOR, color=WRITING_COLOR, width=WIDTH, height=HEIGHT):
    x = width//3
    y = height//1.5
    w = width//3
    h = height//10

    # Initialize two players who each gets a random color
    player_1 = Player(1)
    player_2 = Player(2)

    # Make sure each player gets a different color
    while player_2.color == player_1.color:
        player_2 = Player(2)

    input_box_1 = InputBox(1)
    input_box_2 = InputBox(2)

    done = False

    while not done:
        win.fill(bgcolor)
        input_box_1.draw()
        input_box_2.draw()

        ready_button = make_rect(x, y, w, h)
        draw_rect(ready_button)
        write_text("READY", x, y, w, h)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif is_ready(event, ready_button) and player_1.color != player_2.color:
                done = True
            else:
                update_player(player_1, input_box_1, event)
                update_player(player_2, input_box_2, event)
    return player_1, player_2