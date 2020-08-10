# Author: Andrew Lim
# Version: 08/09/2020
# Description: A program that will engage the user in a 2-person game of Pentago.
# The program uses a minimax approach with several-move look-ahead and alpha-beta pruning.

from GameBoard import GameBoard
import copy
import Minimax

first_player = None
first_color = None
second_player = None
second_color = None

def main():
    get_player_information()

    block_1 = [['.']*3 for i in range(3)]
    block_2 = [['.']*3 for i in range(3)]
    block_3 = [['.']*3 for i in range(3)]
    block_4 = [['.']*3 for i in range(3)]

    board = GameBoard(block_1, block_2, block_3, block_4, None, None, [])

    current_color = first_color

    if first_player == '1':
        move = input('Your move (' + first_color + ') : ')
        game_block = move[0:1]
        position = move[2:3]
        rotation_block = move[4:5]
        direction = move[5:]

        if game_block == '1':
            game_block = block_1
        elif game_block == '2':
            game_block = block_2
        elif game_block == '3':
            game_block = block_3
        else:
            game_block = block_4

        if rotation_block == '1':
            rotation_block = block_1
        elif rotation_block == '2':
            rotation_block = block_2
        elif rotation_block == '3':
            rotation_block = block_3
        else:
            rotation_block = block_4

        board.move(first_color, game_block, int(position))
        if direction == 'L':
            board.rotate_left(rotation_block)
        else:
            board.rotate_right(rotation_block)

        board.print_state()

        current_color = second_color

    max_color = None
    min_color = None
    if first_player == '1':
        max_color = second_color
        min_color = first_color
    else:
        max_color = first_color
        min_color = second_color

    while True:
        # AI's move
        generate_tree(board, 4, current_color)
        board = Minimax.minimax_decision(board, max_color, min_color)
        print("AI's move (" + max_color + ") : ")
        board.print_state()
        if Minimax.terminal_test(board) != 'p':
            break
        
        # human's move
        if current_color == 'w':
            current_color = 'b'
        else:
            current_color = 'w'
        get_player_move(board, current_color)
        board.print_state()
        board.child_nodes = []
        board.utility = None
        if Minimax.terminal_test(board) != 'p':
            break
        if current_color == 'w':
            current_color = 'b'
        else:
            current_color = 'w'
    win_state = Minimax.terminal_test(board)
    print('Game over.')
    if win_state == 't':
        print('Tied.')
    else:
        print('Winner: ' + win_state)

def get_player_move(state, color):
    move = input('Your move (' + color + ') : ')
    game_block = move[0:1]
    position = move[2:3]
    rotation_block = move[4:5]
    direction = move[5:]

    if game_block == '1':
        game_block = state.game_block_1
    elif game_block == '2':
        game_block = state.game_block_2
    elif game_block == '3':
        game_block = state.game_block_3
    else:
        game_block = state.game_block_4

    if rotation_block == '1':
        rotation_block = state.game_block_1
    elif rotation_block == '2':
        rotation_block = state.game_block_2
    elif rotation_block == '3':
        rotation_block = state.game_block_3
    else:
        rotation_block = state.game_block_4

    state.move(color, game_block, int(position))

    if Minimax.terminal_test(state) != 'p':
        return

    if direction == 'L':
        state.rotate_left(rotation_block)
    else:
        state.rotate_right(rotation_block)

def generate_tree(node, depth, color):
    if depth != 0:
        temp = copy.deepcopy(node)
        # game block 1
        for i in range(1, 10):
            if node.available_position(node.game_block_1, i):
                for j in range(8):
                    child_node = copy.deepcopy(temp)
                    child_node.move(color, child_node.game_block_1, i)
                    rotations(child_node, j)
                    node.child_nodes.append(child_node)
                    next_depth = depth - 1
                    if color == 'w':
                        generate_tree(child_node, next_depth, 'b')
                    else:
                        generate_tree(child_node, next_depth, 'w')

        # game block 2
        for i in range(1, 10):
            if node.available_position(node.game_block_2, i):
                for j in range(8):
                    child_node = copy.deepcopy(temp)
                    child_node.move(color, child_node.game_block_2, i)
                    rotations(child_node, j)
                    node.child_nodes.append(child_node)
                    next_depth = depth - 1
                    if color == 'w':
                        generate_tree(child_node, next_depth, 'b')
                    else:
                        generate_tree(child_node, next_depth, 'w')

        # game block 3
        for i in range(1, 10):
            if node.available_position(node.game_block_3, i):
                for j in range(8):
                    child_node = copy.deepcopy(temp)
                    child_node.move(color, child_node.game_block_3, i)
                    rotations(child_node, j)
                    node.child_nodes.append(child_node)
                    next_depth = depth - 1
                    if color == 'w':
                        generate_tree(child_node, next_depth, 'b')
                    else:
                        generate_tree(child_node, next_depth, 'w')

        # game block 4
        for i in range(1, 10):
            if node.available_position(node.game_block_4, i):
                for j in range(8):
                    child_node = copy.deepcopy(temp)
                    child_node.move(color, child_node.game_block_4, i)
                    rotations(child_node, j)
                    node.child_nodes.append(child_node)
                    next_depth = depth - 1
                    if color == 'w':
                        generate_tree(child_node, next_depth, 'b')
                    else:
                        generate_tree(child_node, next_depth, 'w')

def rotations(node, j):
    if j == 0:
        node.rotate_left(node.game_block_1)
    elif j == 1:
        node.rotate_right(node.game_block_1)
    elif j == 2:
        node.rotate_left(node.game_block_2)
    elif j == 3:
        node.rotate_right(node.game_block_2)
    elif j == 4:
        node.rotate_left(node.game_block_3)
    elif j == 5:
        node.rotate_right(node.game_block_3)
    elif j == 6:
        node.rotate_left(node.game_block_4)
    else:
        node.rotate_right(node.game_block_4)

def get_player_information():
    global first_player
    global first_color
    global second_player
    global second_color
    first_player = input('Who moves first? 1. Human (you) 2. AI : ')
    human_color = input('Your token color (b or w) : ')
    # if human goes first
    if first_player == '1':
        first_color = human_color
        second_player = 2
        if human_color == 'b':
            second_color = 'w'
        else:
            second_color = 'b'
    # if AI goes first
    else:
        if human_color == 'b':
            first_color = 'w'
        else:
            first_color = 'b'
        second_player = 1
        second_color = human_color

if __name__ == '__main__':
    main()
