# Jogo da Cobrinha para Termux funcional 

import os
import random
import curses

# Configuração da tela
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Inicialização da cobrinha e comida
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

# Loop principal do jogo
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Verifica a posição da cobrinha
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Verifica se a cobrinha colidiu com as bordas ou com ela mesma
    if (new_head[0] in [0, sh] or
            new_head[1] in [0, sw] or
            new_head in snake):
        curses.endwin()
        quit()

    # Adiciona a nova cabeça da cobrinha
    snake.insert(0, new_head)

    # Verifica se a cobrinha comeu a comida
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    else:
        # Remove a cauda da cobrinha
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Desenha a cobrinha
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
