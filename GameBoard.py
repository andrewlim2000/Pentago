# Author: Andrew Lim
# Version: 08/09/2020
# Description: Representation of a Pentago game board. Implemented with four
# 3x3 game boards.

import copy

class GameBoard():
    def __init__(self, game_block_1, game_block_2, game_block_3, game_block_4, 
        utility, parent_node, child_nodes):
        self.game_block_1 = game_block_1
        self.game_block_2 = game_block_2
        self.game_block_3 = game_block_3
        self.game_block_4 = game_block_4
        self.utility = utility
        self.parent_node = parent_node
        self.child_nodes = child_nodes

    # returns false if position is already taken
    def move(self, player, game_block, position):
        position -= 1
        game_block[position // 3][position % 3] = player

    def available_position(self, game_block, position):
        position -= 1
        if game_block[position // 3][position % 3] == '.':
            return True
        else: 
            return False

    def rotate_left(self, game_block):
        temp = copy.deepcopy(game_block)
        for i in range(3):
            for j in range(3):
                if i == 0:
                    game_block[i][j] = temp[j][2]
                elif i == 1:
                    game_block[i][j] = temp[j][1]
                else:
                    game_block[i][j] = temp[j][0]

    def rotate_right(self, game_block):
        temp = copy.deepcopy(game_block)
        for i in range(3):
            for j in range(3):
                if j == 0:
                    game_block[i][j] = temp[2][i]
                elif j == 1:
                    game_block[i][j] = temp[1][i]
                else:
                    game_block[i][j] = temp[0][i]    

    def print_state(self):
        print('+-------+-------+')
        for i in range(3):
            print('| ' + self.game_block_1[i][0] + ' ' + self.game_block_1[i][1] + ' ' + 
                self.game_block_1[i][2] + ' | ' + self.game_block_2[i][0] + ' ' + 
                self.game_block_2[i][1] + ' ' + self.game_block_2[i][2] + ' |')
        print('+-------+-------+')
        for i in range(3):
            print('| ' + self.game_block_3[i][0] + ' ' + self.game_block_3[i][1] + ' ' + 
                self.game_block_3[i][2] + ' | ' + self.game_block_4[i][0] + ' ' + 
                self.game_block_4[i][1] + ' ' + self.game_block_4[i][2] + ' |')
        print('+-------+-------+')
