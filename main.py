import copy
import pygame
import random

from Player import Player
from Tile import Tile
from Dictionary import Dictionary

# TODO
# pass turn, shuffle tiles, exchange equal tile from the bag, game over
# Blank tiles can be used as any single letter
TILE_WIDTH = 0
TILE_HEIGHT = 0
first_move = True


def init_tiles():
    tiles = []
    for i in range(9):
        tiles.append(Tile('A'))
    for i in range(2):
        tiles.append(Tile('B'))
    for i in range(2):
        tiles.append(Tile('C'))
    for i in range(4):
        tiles.append(Tile('D'))
    for i in range(12):
        tiles.append(Tile('E'))
    for i in range(2):
        tiles.append(Tile('F'))
    for i in range(3):
        tiles.append(Tile('G'))
    for i in range(2):
        tiles.append(Tile('H'))
    for i in range(9):
        tiles.append(Tile('I'))
    for i in range(1):
        tiles.append(Tile('J'))
    for i in range(1):
        tiles.append(Tile('K'))
    for i in range(4):
        tiles.append(Tile('L'))
    for i in range(2):
        tiles.append(Tile('M'))
    for i in range(6):
        tiles.append(Tile('N'))
    for i in range(8):
        tiles.append(Tile('O'))
    for i in range(2):
        tiles.append(Tile('P'))
    for i in range(1):
        tiles.append(Tile('Q'))
    for i in range(6):
        tiles.append(Tile('R'))
    for i in range(4):
        tiles.append(Tile('S'))
    for i in range(6):
        tiles.append(Tile('T'))
    for i in range(4):
        tiles.append(Tile('U'))
    for i in range(2):
        tiles.append(Tile('V'))
    for i in range(2):
        tiles.append(Tile('W'))
    for i in range(1):
        tiles.append(Tile('X'))
    for i in range(2):
        tiles.append(Tile('Y'))
    for i in range(1):
        tiles.append(Tile('Z'))
    for i in range(2):
        tiles.append(Tile(' '))
    return tiles


def init_board(num_tiles):
    global TILE_WIDTH, TILE_HEIGHT
    board = [[Tile('') for i in range(num_tiles)] for j in range(num_tiles)]
    offset = 100
    # -1 to try and fix the int division problem of tile clipping off screen
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            # plus one below is to offset between the tile for grid effect
            board[i][j].x = (j * (TILE_WIDTH + 1)) + offset
            board[i][j].y = (i * (TILE_HEIGHT + 1)) + offset
            board[i][j].width = TILE_WIDTH
            board[i][j].height = TILE_HEIGHT
    board[0][0].set_word_score(3)
    board[1][1].set_word_score(2)
    board[2][2].set_word_score(2)
    board[3][3].set_word_score(2)
    board[4][4].set_word_score(2)
    board[5][5].set_letter_score(3)
    board[6][6].set_letter_score(2)
    board[7][7].set_word_score(2)
    board[8][8].set_letter_score(2)
    board[9][9].set_letter_score(3)
    board[10][10].set_word_score(2)
    board[11][11].set_word_score(2)
    board[12][12].set_word_score(2)
    board[13][13].set_word_score(2)
    board[14][14].set_word_score(3)

    board[0][14].set_word_score(3)
    board[1][13].set_word_score(2)
    board[2][12].set_word_score(2)
    board[3][11].set_word_score(2)
    board[4][10].set_word_score(2)
    board[5][9].set_letter_score(3)
    board[6][8].set_letter_score(2)
    board[8][6].set_letter_score(2)
    board[9][5].set_letter_score(3)
    board[10][4].set_word_score(2)
    board[11][3].set_word_score(2)
    board[12][2].set_word_score(2)
    board[13][1].set_word_score(2)
    board[14][0].set_word_score(3)

    board[0][7].set_word_score(3)
    board[1][5].set_letter_score(3)
    board[1][9].set_letter_score(3)
    board[2][6].set_letter_score(2)
    board[2][8].set_letter_score(2)
    board[3][7].set_letter_score(2)

    board[7][14].set_word_score(3)
    board[5][13].set_letter_score(3)
    board[9][13].set_letter_score(3)
    board[8][12].set_letter_score(2)
    board[6][12].set_letter_score(2)
    board[7][11].set_letter_score(2)

    board[14][7].set_word_score(3)
    board[13][5].set_letter_score(3)
    board[13][9].set_letter_score(3)
    board[12][6].set_letter_score(2)
    board[12][8].set_letter_score(2)
    board[11][7].set_letter_score(2)

    board[7][0].set_word_score(3)
    board[5][1].set_letter_score(3)
    board[9][1].set_letter_score(3)
    board[8][2].set_letter_score(2)
    board[6][2].set_letter_score(2)
    board[7][3].set_letter_score(2)

    board[0][3].set_letter_score(2)
    board[0][11].set_letter_score(2)
    board[3][14].set_letter_score(2)
    board[11][14].set_letter_score(2)
    board[14][11].set_letter_score(2)
    board[14][3].set_letter_score(2)
    board[11][0].set_letter_score(2)
    board[3][0].set_letter_score(2)
    return board


def fill_rack(tiles, player):
    needed_tiles = 7 - len(player.rack)
    for i in range(needed_tiles):
        rand_num = random.randint(0, len(tiles)-1)
        player.rack.append(tiles[rand_num])
        del tiles[rand_num]
    return


def set_player_rack_positions(player):
    global TILE_WIDTH, TILE_HEIGHT
    for i in range(len(player.rack)):
        if (player.rack_direction == 0):
            player.rack[i].set_position(
                (i * (TILE_WIDTH + 1)) + player.rack_start_pos[0], player.rack_start_pos[1])
        else:
            player.rack[i].set_position(
                player.rack_start_pos[0], (i * (TILE_HEIGHT + 1)) + player.rack_start_pos[1])
        player.rack[i].width = TILE_WIDTH
        player.rack[i].height = TILE_HEIGHT
    return


def init_players(board, tiles, num_players):
    global TILE_WIDTH, TILE_HEIGHT
    players = []
    offset = 100
    for i in range(num_players):
        player = Player()
        fill_rack(tiles, player)
        if i == 0:  # Player 0 is below the board
            x = offset + ((len(board) - len(player.rack)) //
                          2) * (TILE_WIDTH + 1)
            y = offset + 10 + (len(board)) * (TILE_HEIGHT + 1)
            player.rack_direction = 0
        elif i == 1:  # Player 1 is to the left of the board
            x = offset - 10 - (TILE_WIDTH + 1)
            y = offset + ((len(board) - len(player.rack)) //
                          2) * (TILE_HEIGHT + 1)
            player.rack_direction = 1
        elif i == 2:  # Player 2 is above the board
            x = offset + ((len(board) - len(player.rack)) //
                          2) * (TILE_WIDTH + 1)
            y = offset - 10 - (TILE_HEIGHT + 1)
            player.rack_direction = 0
        elif i == 3:  # Player 3 is to the right of the board
            x = offset + 10 + (len(board)) * (TILE_WIDTH + 1)
            y = offset + ((len(board) - len(player.rack)) //
                          2) * (TILE_HEIGHT + 1)
            player.rack_direction = 1
        player.rack_start_pos = (x, y)
        set_player_rack_positions(player)
        players.append(player)
    return players


def get_going(tiles, num_players):
    # TODO
    # blank tile wins start of the game
    best = 91  # min value 31 max value 90 (unicode)
    going = 0
    for i in range(num_players):
        score = ord('A') - \
            ord(tiles[random.randint(0, len(tiles)-1)].character)
        if (score < best):
            best = score
            going = i
    return going


def score_word(dictionary, word):
    score = 0
    for char in word:
        score += dictionary[char]
    return score


def get_adjacent_letters(board, x, y, dx, dy):
    word = ""
    while (0 <= x < len(board) and 0 <= y < len(board[0]) and board[y][x].character != ''):
        word += board[y][x].character
        x += dx
        y += dy
    if (dx < 0 or dy < 0):
        return word[::-1]
    return word


def get_between(board, x, y, dx, dy, end_x, end_y):
    word = ""
    while(0 <= x < len(board) and 0 <= y < len(board[0]) and x < end_x and y < end_y):
        word+=board[y][x].character
        x+=dx
        y+=dy
    return word


def valid_move(dictionary, board, history):
    if(not history or len(history) < 2):
        print("word needs to be a minimum of 2 letters long")
        return False
    global first_move
    adjacent_words = []
    word = ""
    intersections = 0
    touches_center = False
    history.sort(key=lambda pos: pos[0][1])
    # direction: 0 - horizontal, 1 - vertical
    direction = 1 if history[0][0][1][0] == history[len(history)-1][0][1][0] else (0 if history[0][0][1][1] == history[len(history)-1][0][1][1] else None)
    for i in range(len(history)):
        x = history[i][0][1][0]
        y = history[i][0][1][1]
        if(first_move and x == 7 and y == 7):
            touches_center = True
        if(i == 0):
            pass
        else:
            prev_x = history[i-1][0][1][0]
            prev_y = history[i-1][0][1][1]
            if(x == prev_x):
                if(y - prev_y != 1):
                    chars_between = get_between(board, prev_x, prev_y + 1, 0, 1, x+1, y)
                    if(chars_between == ""):
                        print("Invalid word vertical gap between letters")
                        return False
                    else:
                        word += chars_between
                        intersections += 1
                direction = 1
            elif(y == prev_y):
                if(x - prev_x != 1):
                    chars_between = get_between(board, prev_x + 1, prev_y, 1, 0, x, y+1)
                    if(chars_between == ""):
                        print("Invalid word horizontal gap between letters")
                        return False
                    else:
                        word += chars_between
                        intersections += 1
                direction = 0
            else:
                print("Invalid tiles change direction")
                return False
        word += board[y][x].character
        adjacent_tile = ""
        if (direction == 0):
            adjacent_tile = get_adjacent_letters(board, x, y - 1, 0, -1) + board[y][x].character + get_adjacent_letters(board, x, y + 1, 0, 1)
        elif (direction == 1):
            adjacent_tile = get_adjacent_letters(board, x - 1, y, -1, 0) + board[y][x].character + get_adjacent_letters(board, x + 1, y, 1, 0)
        if (adjacent_tile != board[y][x].character):
            intersections+=1
            adjacent_words.append(adjacent_tile)
    adjacent_tile = ""
    if (direction == 0):
        adjacent_tile = get_adjacent_letters(board, history[0][0][1][0] - 1, history[0][0][1][1], -1, 0) + word + get_adjacent_letters(board, history[len(history)-1][0][1][0] + 1, history[len(history)-1][0][1][1], 1, 0)
    elif (direction == 1):
        adjacent_tile = get_adjacent_letters(board, history[0][0][1][0], history[0][0][1][1] - 1, 0, -1) + word + get_adjacent_letters(board, history[len(history)-1][0][1][0], history[len(history)-1][0][1][1] + 1, 0, 1)
    if (adjacent_tile != word):
        intersections+=1
        word = adjacent_tile
    else:
        adjacent_words.append(word)
    for w in adjacent_words:
        result = dictionary.word_in_dictionary(w.lower())
        if(not result):
            print(w, "is not in the dictionary")
            return False
    if(first_move and not touches_center):
        print("word must be played in the center of the board")
        return False
    elif(not first_move and intersections == 0):
        print("word must intersect at least one tile on the board that has already been played")
        return False
    first_move = False
    return True


def reset_move(board, history):
    # record object from history stack
    # (board obj, prev (x, y) in board array),(player that played the tile, prev index of tile in player.rack)
    if not history:
        return
    record = history.pop()
    board_obj = record[0]
    player_obj = record[1]
    tile = board[board_obj[1][1]][board_obj[1][0]]
    tile.reset_previous()
    player_obj[0].rack[player_obj[1]] = tile

    board[board_obj[1][1]][board_obj[1][0]] = board_obj[0]
    return


def mouse(board, history, players, selected_tile, position, going):
    for i in range(len(players)):
        for j in range(len(players[i].rack)):
            if (players[i].rack[j] is not None and players[i].rack[j].collision(position[0], position[1]) and going == i):
                if (selected_tile[0] is not None):
                    selected_tile[0].selected = False
                selected_tile[0] = players[i].rack[j]
                selected_tile[0].selected = True
                break
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j].collision(position[0], position[1]) and selected_tile[0] is not None and board[i][j].character == ''):
                board[i][j].set_previous()
                selected_tile[0].set_previous()
                player_tile_idx = players[going].rack.index(selected_tile[0])
                history.append(((copy.copy(board[i][j]), (j, i)), (players[going], player_tile_idx)))
                selected_tile[0].selected = False
                selected_tile[0].set_position(board[i][j].x, board[i][j].y)
                board[i][j] = selected_tile[0]
                players[going].rack[player_tile_idx] = None
                selected_tile[0] = None
                break
    return


def render(screen, font, board, players, submit_button):
    screen.fill(pygame.Color('black'))  # clear the screen from previous frame
    for row in board:
        for tile in row:
            tile.render(screen, font)

    for player in players:
        player.render(screen, font)

    text_surface = font.render("submit", False, (0, 0, 0))
    pygame.draw.rect(screen, (227, 207, 170), submit_button)
    screen.blit(text_surface, (submit_button[0], submit_button[1], submit_button[0] + (submit_button[2]//2), submit_button[1] + (submit_button[3]//2)))
    pygame.display.flip()
    return


def main():
    global TILE_WIDTH, TILE_HEIGHT
    tile_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
                   'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, ' ': 0}
    dictionary = Dictionary()
    pygame.init()
    WIDTH, HEIGHT, OFFSET, ROW_LEN, NUM_PLAYERS = 800, 800, 100, 15, 2
    TILE_WIDTH = ((WIDTH-(2*OFFSET))//ROW_LEN)
    TILE_HEIGHT = ((HEIGHT-(2*OFFSET))//ROW_LEN)
    tiles = init_tiles()
    board = init_board(ROW_LEN)
    players = init_players(board, tiles, NUM_PLAYERS)
    going = get_going(tiles, NUM_PLAYERS)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("monospace", 15)
    running = True
    button = (WIDTH - 100, HEIGHT - 50, 80, 40)
    # since this language has no obj pass by reference need to put it in list to pass by reference or global variable
    selected_tile = [None]
    history = []  # save previous moves incase player undos move
    pygame.display.set_caption('Scrabble')
    print("Player {}s Turn".format(going+1))
    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse(board, history, players, selected_tile, pygame.mouse.get_pos(), going)
                if (button[0] <= pygame.mouse.get_pos()[0] <= button[0] + button[2] and button[1] <= pygame.mouse.get_pos()[1] <= button[1] + button[3]):
                    if (valid_move(dictionary, board, history)):
                        history.clear()
                        players[going].rack = [tile for tile in players[going].rack if tile is not None]
                        fill_rack(tiles, players[going])
                        set_player_rack_positions(players[going])
                        print("Player {}s Turn".format(going+1))
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    reset_move(board, history)
        render(screen, font, board, players, button)
    dictionary.close()
    pygame.quit()
    return


main()
