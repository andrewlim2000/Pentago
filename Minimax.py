# Author: Andrew Lim
# Version: 08/09/2020
# Description: Minimax algorithm.

def minimax_decision(state, max_color, min_color):
    value = max_value(state, float('-inf'), float('inf'), max_color, min_color)
    for node in state.child_nodes:
        if node.utility == value:
            return node

def utility(state, player, max_color, min_color):
    win_state = terminal_test(state)
    # if terminal node
    if win_state != 'p':
        if win_state == 't':
            state.utility = 0
            return 0
        elif player == 'max':
            state.utility = float('inf')
            return float('inf')
        else:
            state.utility = float('-inf')
            return float('-inf')
    else:
        # put all 4 game blocks into 1 big 6x6 game block for easier computation
        temp_board = [['.']*6 for i in range(6)]
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = state.game_block_1[i][j]
        for i in range(3):
            for j in range(3, 6):
                temp_board[i][j] = state.game_block_2[i][j - 3]
        for i in range(3, 6):
            for j in range(3):
                temp_board[i][j] = state.game_block_3[i - 3][j]
        for i in range(3, 6):
            for j in range(3, 6):
                temp_board[i][j] = state.game_block_4[i - 3][j - 3]

        # max
        max_utility = 0

        # rows
        current_count = 0
        max_count = 0
        for i in range(6):
            for j in range(5):
                if temp_board[i][j] == max_color and temp_board[i][j] == temp_board[i][j + 1]:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    current_count = 0
                    max_count = max(max_count, current_count)
        max_utility += max_count

        # columns
        current_count = 0
        max_count = 0
        for i in range(6):
            for j in range(5):
                if temp_board[j][i] == max_color and temp_board[j][i] == temp_board[j + 1][i]:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    current_count = 0
                    max_count = max(max_count, current_count)
        max_utility += max_count

        # diagonals
        current_count = 0
        max_count = 0
        for i in range(5):
            if temp_board[i][i] == max_color and temp_board[i][i] == temp_board[i + 1][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count
        
        current_count = 0
        max_count = 0
        for i in range(1, 5):
            if temp_board[i][i - 1] == max_color and temp_board[i][i - 1] == temp_board[i + 1][i]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count

        current_count = 0
        max_count = 0
        for i in range(4):
            if temp_board[i][i + 1] == max_color and temp_board[i][i + 1] == temp_board[i + 1][i + 2]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count

        ##########
        current_count = 0
        max_count = 0
        for i in range(5):
            if temp_board[5 - i][i] == max_color and temp_board[5 - i][i] == temp_board[4 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count
        
        current_count = 0
        max_count = 0
        for i in range(1, 5):
            if temp_board[6 - i][i] == max_color and temp_board[6 - i][i] == temp_board[5 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count

        current_count = 0
        max_count = 0
        for i in range(4):
            if temp_board[4 - i][i] == max_color and temp_board[4 - i][i] == temp_board[3 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        max_utility += max_count

        # min
        min_utility = 0

        # rows
        current_count = 0
        max_count = 0
        for i in range(6):
            for j in range(5):
                if temp_board[i][j] == min_color and temp_board[i][j] == temp_board[i][j + 1]:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    current_count = 0
                    max_count = max(max_count, current_count)
        min_utility += max_count

        # columns
        current_count = 0
        max_count = 0
        for i in range(6):
            for j in range(5):
                if temp_board[j][i] == min_color and temp_board[j][i] == temp_board[j + 1][i]:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    current_count = 0
                    max_count = max(max_count, current_count)
        min_utility += max_count

        # diagonals
        current_count = 0
        max_count = 0
        for i in range(5):
            if temp_board[i][i] == min_color and temp_board[i][i] == temp_board[i + 1][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count
        
        current_count = 0
        max_count = 0
        for i in range(1, 5):
            if temp_board[i][i - 1] == min_color and temp_board[i][i - 1] == temp_board[i + 1][i]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count

        current_count = 0
        max_count = 0
        for i in range(4):
            if temp_board[i][i + 1] == min_color and temp_board[i][i + 1] == temp_board[i + 1][i + 2]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count

        ##########
        current_count = 0
        max_count = 0
        for i in range(5):
            if temp_board[5 - i][i] == min_color and temp_board[5 - i][i] == temp_board[4 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count
        
        current_count = 0
        max_count = 0
        for i in range(1, 5):
            if temp_board[6 - i][i] == min_color and temp_board[6 - i][i] == temp_board[5 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count

        current_count = 0
        max_count = 0
        for i in range(4):
            if temp_board[4 - i][i] == min_color and temp_board[4 - i][i] == temp_board[3 - i][i + 1]:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                max_count = max(max_count, current_count)
        min_utility += max_count
        state.utility = max_utility - min_utility
        return state.utility

def max_value(state, alpha, beta, max_color, min_color):
    # if leaf node
    if len(state.child_nodes) == 0:
        return utility(state, 'max', max_color, min_color)
    best_value = float('-inf')
    for node in state.child_nodes:
        value = min_value(node, alpha, beta, max_color, min_color)
        best_value = max(best_value, value)
        alpha = max(alpha, best_value)
        state.utility = value
        if beta <= alpha:
            break
    return best_value

def min_value(state, alpha, beta, max_color, min_color):
    # if leaf node
    if len(state.child_nodes) == 0:
        return utility(state, 'min', max_color, min_color)
    best_value = float('inf')
    for node in state.child_nodes:
        value = max_value(node, alpha, beta, max_color, min_color)
        best_value = min(best_value, value)
        beta = min(beta, best_value)
        state.utility = value
        if beta <= alpha:
            break
    return best_value

# returns 'w' if white won
# returns 'b' if black won
# returns 't' if tied
# returns 'p' if game is still in progress
def terminal_test(state):
    result = 'p'
    # check rows
    for i in range(6):
        # game block 1 and game block 2
        if i // 3 == 0:
            if (state.game_block_1[i % 3][0] != '.'
                and state.game_block_1[i % 3][0] == state.game_block_1[i % 3][1]
                and state.game_block_1[i % 3][1] == state.game_block_1[i % 3][2]
                and state.game_block_1[i % 3][2] == state.game_block_2[i % 3][0]
                and state.game_block_2[i % 3][0] == state.game_block_2[i % 3][1]) or (state.game_block_1[i % 3][1] != '.'
                and state.game_block_1[i % 3][1] == state.game_block_1[i % 3][2]
                and state.game_block_1[i % 3][2] == state.game_block_2[i % 3][0]
                and state.game_block_2[i % 3][0] == state.game_block_2[i % 3][1]
                and state.game_block_2[i % 3][1] == state.game_block_2[i % 3][2]):
                # check for tie
                if result != 'p' and result != state.game_block_1[i % 3][1]:
                    return 't'
                else:
                    result = state.game_block_1[i % 3][1]
        # game block 3 and game block 4
        else:
            if (state.game_block_3[i % 3][0] != '.'
                and state.game_block_3[i % 3][0] == state.game_block_3[i % 3][1]
                and state.game_block_3[i % 3][1] == state.game_block_3[i % 3][2]
                and state.game_block_3[i % 3][2] == state.game_block_4[i % 3][0]
                and state.game_block_4[i % 3][0] == state.game_block_4[i % 3][1]) or (state.game_block_3[i % 3][1] != '.'
                and state.game_block_3[i % 3][1] == state.game_block_3[i % 3][2]
                and state.game_block_3[i % 3][2] == state.game_block_4[i % 3][0]
                and state.game_block_4[i % 3][0] == state.game_block_4[i % 3][1]
                and state.game_block_4[i % 3][1] == state.game_block_4[i % 3][2]):
                # check for tie
                if result != 'p' and result != state.game_block_3[i % 3][1]:
                    return 't'
                else:
                    result = state.game_block_3[i % 3][1]
                
    # check columns
    for i in range(6):
        # game block 1 and game block 3
        if i // 3 == 0:
            if (state.game_block_1[0][i % 3] != '.'
                and state.game_block_1[0][i % 3] == state.game_block_1[1][i % 3]
                and state.game_block_1[1][i % 3] == state.game_block_1[2][i % 3]
                and state.game_block_1[2][i % 3] == state.game_block_3[0][i % 3]
                and state.game_block_3[0][i % 3] == state.game_block_3[1][i % 3]) or (state.game_block_1[1][i % 3] != '.'
                and state.game_block_1[1][i % 3] == state.game_block_1[2][i % 3]
                and state.game_block_1[2][i % 3] == state.game_block_3[0][i % 3]
                and state.game_block_3[0][i % 3] == state.game_block_3[1][i % 3]
                and state.game_block_3[1][i % 3] == state.game_block_3[2][i % 3]):
                # check for tie
                if result != 'p' and result != state.game_block_1[1][i % 3]:
                    return 't'
                else:
                    result = state.game_block_1[1][i % 3]
        # game block 2 and game block 4
        else:
            if (state.game_block_2[0][i % 3] != '.'
                and state.game_block_2[0][i % 3] == state.game_block_2[1][i % 3]
                and state.game_block_2[1][i % 3] == state.game_block_2[2][i % 3]
                and state.game_block_2[2][i % 3] == state.game_block_4[0][i % 3]
                and state.game_block_4[0][i % 3] == state.game_block_4[1][i % 3]) or (state.game_block_2[1][i % 3] != '.'
                and state.game_block_2[1][i % 3] == state.game_block_2[2][i % 3]
                and state.game_block_2[2][i % 3] == state.game_block_4[0][i % 3]
                and state.game_block_4[0][i % 3] == state.game_block_4[1][i % 3]
                and state.game_block_4[1][i % 3] == state.game_block_4[2][i % 3]):
                # check for tie
                if result != 'p' and result != state.game_block_2[1][i % 3]:
                    return 't'
                else:
                    result = state.game_block_2[1][i % 3]
    # check diagonal
    # \ diagonals
    if (state.game_block_1[0][0] != '.'
        and state.game_block_1[0][0] == state.game_block_1[1][1]
        and state.game_block_1[1][1] == state.game_block_1[2][2]
        and state.game_block_1[2][2] == state.game_block_4[0][0]
        and state.game_block_4[0][0] == state.game_block_4[1][1]) or (state.game_block_1[1][1] != '.'
        and state.game_block_1[1][1] == state.game_block_1[2][2]
        and state.game_block_1[2][2] == state.game_block_4[0][0]
        and state.game_block_4[0][0] == state.game_block_4[1][1]
        and state.game_block_4[1][1] == state.game_block_4[2][2]):
        # check for tie
        if result != 'p' and result != state.game_block_1[1][1]:
            return 't'
        else:
            result = state.game_block_1[1][1]
    
    if (state.game_block_1[1][0] != '.'
        and state.game_block_1[1][0] == state.game_block_1[2][1]
        and state.game_block_1[2][1] == state.game_block_3[0][2]
        and state.game_block_3[0][2] == state.game_block_4[1][0]
        and state.game_block_4[1][0] == state.game_block_4[2][1]):
        # check for tie
        if result != 'p' and result != state.game_block_1[1][0]:
            return 't'
        else:
            result = state.game_block_1[1][0]

    if (state.game_block_1[0][1] != '.'
        and state.game_block_1[0][1] == state.game_block_1[1][2]
        and state.game_block_1[1][2] == state.game_block_2[2][0]
        and state.game_block_2[2][0] == state.game_block_4[0][1]
        and state.game_block_4[0][1] == state.game_block_4[1][2]):
        # check for tie
        if result != 'p' and result != state.game_block_1[0][1]:
            return 't'
        else:
            result = state.game_block_1[0][1]

    # / diagonals
    if (state.game_block_2[0][2] != '.'
        and state.game_block_2[0][2] == state.game_block_2[1][1]
        and state.game_block_2[1][1] == state.game_block_2[2][0]
        and state.game_block_2[2][0] == state.game_block_3[0][2]
        and state.game_block_3[0][2] == state.game_block_3[1][1]) or (state.game_block_2[1][1] != '.'
        and state.game_block_2[1][1] == state.game_block_2[2][0]
        and state.game_block_2[2][0] == state.game_block_3[0][2]
        and state.game_block_3[0][2] == state.game_block_3[1][1]
        and state.game_block_3[1][1] == state.game_block_3[2][0]):
        # check for tie
        if result != 'p' and result != state.game_block_2[1][1]:
            return 't'
        else:
            result = state.game_block_2[1][1]
    
    if (state.game_block_2[0][1] != '.'
        and state.game_block_2[0][1] == state.game_block_2[1][0]
        and state.game_block_2[1][0] == state.game_block_1[2][2]
        and state.game_block_1[2][2] == state.game_block_3[0][1]
        and state.game_block_3[0][1] == state.game_block_3[1][0]):
        # check for tie
        if result != 'p' and result != state.game_block_2[0][1]:
            return 't'
        else:
            result = state.game_block_2[0][1]

    if (state.game_block_2[1][2] != '.'
        and state.game_block_2[1][2] == state.game_block_2[2][1]
        and state.game_block_2[2][1] == state.game_block_4[0][0]
        and state.game_block_4[0][0] == state.game_block_3[1][2]
        and state.game_block_3[1][2] == state.game_block_3[2][0]):
        # check for tie
        if result != 'p' and result != state.game_block_2[1][2]:
            return 't'
        else:
            result = state.game_block_2[1][2]

    return result
    