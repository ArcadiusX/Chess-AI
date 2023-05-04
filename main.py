
# Import Modules & Libraries
import global_vars as G
import display_gui as gui
import ai_algorithms as ai
import pygame, chess, time, sys, random

pygame.init()
pygame.font.init()
pygame.display.init()

# Game Settings
TEST_MODE = False
AI_DELAY = 0.000000000000000000000000000001
B_DIFFICULTY = -1
W_DIFFICULTY = 0

white = True
while white:

    G.CLOCK.tick(60)

    G.SCREEN.fill((255, 255, 255))
    FONT = pygame.font.Font('images/joystix monospace.ttf', 15)
    instructions = FONT.render('Press 1 for white player control', True, (0, 0, 0))
    instructions1 = FONT.render('Press 2 for white in sandbox mode', True, (0, 0, 0))
    instructions2 = FONT.render('Press 3 for white in Random AI mode', True, (0, 0, 0))
    instructions3 = FONT.render('Press 4 for white in Positional AI mode', True, (0, 0, 0))
    instructions4 = FONT.render('Press 5 for white in Predictive AI mode', True, (0, 0, 0))
    instructions5 = FONT.render('Press 6, 7, 8, or 9 for white in corresponding levels of AI', True, (0, 0, 0))

    G.SCREEN.blit(instructions, (180, 150))
    G.SCREEN.blit(instructions1, (179, 180))
    G.SCREEN.blit(instructions2, (175, 210))
    G.SCREEN.blit(instructions3, (165, 240))
    G.SCREEN.blit(instructions4, (165, 270))
    G.SCREEN.blit(instructions5, (10, 300))


    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                W_DIFFICULTY = -1
                white = False
            if event.key == pygame.K_2:
                W_DIFFICULTY = 0
                white = False
            if event.key == pygame.K_3:
                W_DIFFICULTY = 1
                white = False
            if event.key == pygame.K_4:
                W_DIFFICULTY = 2
                white = False
            if event.key == pygame.K_5:
                W_DIFFICULTY = 3
                white = False
            if event.key == pygame.K_6:
                W_DIFFICULTY = 4
                white = False
            if event.key == pygame.K_7:
                W_DIFFICULTY = 5
                white = False
            if event.key == pygame.K_8:
                W_DIFFICULTY = 6
                white = False
            if event.key == pygame.K_9:
                W_DIFFICULTY = 7
                white = False

black = True
while black:

    G.CLOCK.tick(60)

    G.SCREEN.fill((0, 0, 0))
    FONT = pygame.font.Font('images/joystix monospace.ttf', 15)
    instructions = FONT.render('Press 1 for black player control', True, (255, 255, 255))
    instructions1 = FONT.render('Press 2 for black in sandbox mode', True, (255, 255, 255))
    instructions2 = FONT.render('Press 3 for black in Random AI mode', True, (255, 255, 255))
    instructions3 = FONT.render('Press 4 for black in Positional AI mode', True, (255, 255, 255))
    instructions4 = FONT.render('Press 5 for black in Predictive AI mode', True, (255, 255, 255))
    instructions5 = FONT.render('Press 6, 7, 8, or 9 for black in corresponding levels of AI', True, (255, 255, 255))

    G.SCREEN.blit(instructions, (180, 150))
    G.SCREEN.blit(instructions1, (179, 180))
    G.SCREEN.blit(instructions2, (175, 210))
    G.SCREEN.blit(instructions3, (165, 240))
    G.SCREEN.blit(instructions4, (165, 270))
    G.SCREEN.blit(instructions5, (10, 300))


    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                B_DIFFICULTY = -1
                black = False
            if event.key == pygame.K_2:
                B_DIFFICULTY = 0
                black = False
            if event.key == pygame.K_3:
                B_DIFFICULTY = 1
                black = False
            if event.key == pygame.K_4:
                B_DIFFICULTY = 2
                black = False
            if event.key == pygame.K_5:
                B_DIFFICULTY = 3
                black = False
            if event.key == pygame.K_6:
                B_DIFFICULTY = 4
                black = False
            if event.key == pygame.K_7:
                B_DIFFICULTY = 5
                black = False
            if event.key == pygame.K_8:
                B_DIFFICULTY = 6
                black = False
            if event.key == pygame.K_9:
                B_DIFFICULTY = 7
                black = False

# Board Setup
G.BOARD_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
G.BOARD.set_board_fen(G.BOARD_FEN)
gui.draw_board()
from_square = None
outcome = None

#Difficulty Control Function

def difficulty_options(move, difficulty):
    if difficulty == 0:
        move = chess.Move.null()
    elif difficulty == 1:
        move = ai.select_random()
    elif difficulty == 2:
        move = ai.select_positional()
    elif difficulty > 2:
        move = ai.select_predictive(difficulty - 2)
    if difficulty >= 0:
        ai.make_ai_move(move, AI_DELAY)
    return move

# Pygame Display Loop
while not outcome:
    G.CLOCK.tick(60)
    move = None

    #Player Control Flow
    if G.BOARD.turn == chess.BLACK:
        move = difficulty_options(move, B_DIFFICULTY)
    elif G.BOARD.turn == chess.WHITE:
        move = difficulty_options(move, W_DIFFICULTY)

    # Check Input Events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Reset Highlight on Any Click
            tile_num = gui.tile_pos_to_num(event.pos)
            gui.draw_board()

            # First Click on New Turn -> Select Square
            if from_square == None:
                from_square = gui.make_selection(tile_num)
            # Selected Square Clicked Again -> Unselect Square
            elif from_square == tile_num:
                gui.draw_board()
                from_square = None
            # Potential Move Clicked -> ...
            elif from_square != None:
                # ...If Valid, Highlight & Move Selected Piece
                for move in G.BOARD.legal_moves:
                    if move.from_square == from_square and move.to_square == tile_num:
                        gui.draw_select_square(move.from_square)
                        gui.draw_select_square(move.to_square)
                        gui.print_san(move)
                        G.BOARD.push(move)
                        from_square = None
                # ...If Invalid, Only Select Square Instead
                if from_square != None:
                    from_square = gui.make_selection(tile_num)

        # Window Close -> End Program
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    # Draw All Pieces on Screen
    for piece_type in range(1, 7):
        w_piece_tiles = G.BOARD.pieces(piece_type, chess.WHITE)
        for tile_num in w_piece_tiles:
            gui.draw_piece(tile_num, piece_type, chess.WHITE)

        b_piece_tiles = G.BOARD.pieces(piece_type, chess.BLACK)
        for tile_num in b_piece_tiles:
            gui.draw_piece(tile_num, piece_type, chess.BLACK)

    # Check End Game Conditions
    outcome = G.BOARD.outcome()
    if not TEST_MODE and outcome:
        gui.determine_outcome(outcome)

    # Update the Display Screen
    pygame.display.update()

# Wait till Exit after Game Over
while True:
    G.CLOCK.tick(60)
    for event in pygame.event.get():
        # Window Close -> End Program
        if event.type == pygame.QUIT:
            outcome = True
            pygame.display.quit()
            pygame.quit()
            sys.exit()

