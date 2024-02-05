import pygame
import random

from Player import Player
from Tile import Tile

# TODO
# pass turn, exchange equal tile from the bag, game over

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

def init_board(num_tiles, width, height):
    board = [[Tile('', 0) for i in range(num_tiles)] for j in range(num_tiles)]
    offset = 100
    # -1 to try and fix the int division problem of tile clipping off screen
    tile_width = ((width-(2*offset))//len(board))
    tile_height = ((height-(2*offset))//len(board))
    for i in range(0, len(board), 1):
        for j in range(0, len(board[i]), 1):
            # plus one below is to offset between the tile for grid effect
            board[i][j].x = (j * (tile_width + 1)) + offset
            board[i][j].y = (i * (tile_height + 1)) + offset
            board[i][j].width = tile_width
            board[i][j].height = tile_height
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

def fill_rack(tiles, cur_num_tiles):
    rack = []
    needed_tiles = 7 - cur_num_tiles
    for i in range(needed_tiles):
        rand_num = random.randint(0, len(tiles)-1)
        rack.append(tiles[rand_num])
        del tiles[rand_num]
    return rack

def init_players(board, tiles, num_players, width, height):
    players = []
    offset = 100 
    tile_width = (((width-(2*offset))//len(board)))
    tile_height = (((height-(2*offset))//len(board)))
    for i in range(num_players):
        player = Player()
        player.rack = fill_rack(tiles, len(player.rack))
        if i == 0:  # Player 0 is below the board
            x = offset + ((len(board) - len(player.rack)) // 2) * (tile_width + 1)
            y = offset + 10 + (len(board)) * (tile_height + 1)
        elif i == 1:  # Player 1 is to the left of the board
            x = offset - 10 -  (tile_width + 1)
            y = offset + ((len(board) - len(player.rack)) // 2) * (tile_height + 1)
        elif i == 2:  # Player 2 is above the board
            x = offset + ((len(board) - len(player.rack)) // 2) * (tile_width + 1)
            y = offset - 10 - (tile_height + 1)
        elif i == 3:  # Player 3 is to the right of the board
            x = offset + 10 + (len(board)) * (tile_width + 1)
            y = offset + ((len(board) - len(player.rack)) // 2) * (tile_height + 1)
        for j in range(0, len(player.rack), 1):
                    if i == 0 or i == 2:  # Draw horizontally for players above and below the board
                        player.rack[j].x = (j * (tile_width + 1)) + x
                        player.rack[j].y = y
                    else:  # Draw vertically for players to the left and right of the board
                        player.rack[j].x = x
                        player.rack[j].y = (j * (tile_height + 1)) + y
                    player.rack[j].width = tile_width
                    player.rack[j].height = tile_height
        players.append(player)
    return players

def get_going(tiles, num_players):
    best = 91  # min value 31 max value 90 unicode
    going = 0
    for i in range(num_players):
        score = ord('A') - ord(tiles[random.randint(0, len(tiles)-1)].character)
        if (score < best):
            best = score
            going = i
    return going

def reset_move():
    return

def mouse(board, board_history, players, selected_tile, position, going):
    for i in range(len(players)):
        for j in range(len(players[i].rack)):
            if(players[i].rack[j].collision(position[0], position[1]) and going == i):
                if(selected_tile[0] is not None):
                    selected_tile[0].selected = False   
                selected_tile[0] = players[i].rack[j]
                selected_tile[0].selected = True
                break
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j].collision(position[0], position[1]) and selected_tile[0] is not None and board[i][j].character == ''):
                board[i][j].set_previous()
                board_history.append(board[i][j])
                selected_tile[0].selected = False
                selected_tile[0].set_previous()
                selected_tile[0].set_position(board[i][j].x, board[i][j].y)
                board[i][j] = selected_tile[0]
                selected_tile[0].remove = True
                selected_tile[0] = None
                break
    return

def render(screen, font, board, players, submit_button):
    screen.fill(pygame.Color('black')) # clear the screen from previous frame
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
    tile_values = {'a': 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2,'h': 4,'i': 1,'j': 8,'k': 5,'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,'q': 10,'r': 1,'s': 1,'t': 1,'u': 1,'v': 4,'w': 4,'x': 8,'y': 4,'z': 10,' ': 0}
    pygame.init()
    WIDTH, HEIGHT, ROW_LEN, NUM_PLAYERS = 800, 800, 15, 2
    tiles = init_tiles()
    board = init_board(ROW_LEN, WIDTH, HEIGHT)
    players = init_players(board, tiles, NUM_PLAYERS, WIDTH, HEIGHT)
    going = get_going(tiles, NUM_PLAYERS)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("monospace", 15)
    running = True
    button = (WIDTH - 100, HEIGHT - 50, 80, 40)
    selected_tile = [None] # since this stupid language has no pass by reference need to put it in list to pass by reference or global variable
    board_history = [] # save previous moves incase player undos move
    pygame.display.set_caption('Scrabble')
    print(going)
    while (running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse(board, board_history, players, selected_tile, pygame.mouse.get_pos(), going)         
                for player in players:
                    player.rack = [tile for tile in player.rack if not tile.remove]       
                if(button[0] <= pygame.mouse.get_pos()[0] <= button[0] + button[2] and button[1] <= pygame.mouse.get_pos()[1] <= button[1] + button[3]):
                    # going = (going + 1) % NUM_PLAYERS
                    print("Submit")
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    reset_move()
        render(screen, font, board, players, button)
    pygame.quit()
    return

main()
