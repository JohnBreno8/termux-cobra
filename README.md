esse jogo roda em terminais Linux.
1. Configuração da Tela

stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

curses.initscr(): Inicializa a biblioteca curses e cria uma tela de janela para desenhar.

curses.curs_set(0): Esconde o cursor para não interferir na visualização do jogo.

getmaxyx(): Obtém as dimensões da janela (altura e largura).

newwin(sh, sw, 0, 0): Cria uma nova janela com as dimensões obtidas.

keypad(1): Habilita a detecção de teclas especiais (como as setas).

timeout(100): Define um intervalo de tempo de 100 milissegundos entre as atualizações da tela.


2. Inicialização da Cobrinha e da Comida

""snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)""

Define a posição inicial da cobrinha no meio da tela (começa com três partes: cabeça e corpo).

A comida é posicionada no centro da tela, representada pelo símbolo ACS_PI (um "pí" ou símbolo similar a uma maçã).

A cobrinha é uma lista de coordenadas, onde a cabeça é a primeira posição e as outras partes formam o corpo.


3. Controle do Jogo

key = curses.KEY_RIGHT

Define que a direção inicial da cobrinha será para a direita.


4. Loop Principal

O loop principal do jogo começa com:

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

getch(): Aguarda a entrada do usuário. Se nenhuma tecla for pressionada, mantém a última direção (key).


5. Movimento da Cobrinha

O movimento da cobrinha é calculado conforme a direção:

new_head = [snake[0][0], snake[0][1]]

A nova cabeça é criada com as mesmas coordenadas da cabeça atual.

Com base na direção, a posição da nova cabeça é atualizada:

KEY_DOWN: Move para baixo.

KEY_UP: Move para cima.

KEY_LEFT: Move para a esquerda.

KEY_RIGHT: Move para a direita.



6. Colisão com as Bordas ou com o Corpo

if (new_head[0] in [0, sh] or
        new_head[1] in [0, sw] or
        new_head in snake):
    curses.endwin()
    quit()

O jogo termina se a cobrinha colidir com as bordas ou com ela mesma.


7. Comer a Comida

if snake[0] == food:
    food = None
    while food is None:
        nf = [
            random.randint(1, sh-1),
            random.randint(1, sw-1)
        ]
        food = nf if nf not in snake else None
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

Se a cabeça da cobrinha atingir a comida, ela cresce e a comida é reposicionada aleatoriamente na tela (fora da cobrinha).


8. Remover a Cauda

else:
    tail = snake.pop()
    w.addch(int(tail[0]), int(tail[1]), ' ')

Se a cobrinha não comer a comida, a cauda é removida, e o último segmento da cobrinha (a cauda) é apagado da tela.


9. Desenhar a Cobrinha

w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

A cabeça da cobrinha é desenhada na tela com o símbolo ACS_CKBOARD.

