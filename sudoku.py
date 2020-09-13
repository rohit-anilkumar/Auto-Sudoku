#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:05:48 2020

@author: rohit
"""


def printBoard(board):
    
    for i in range(len(board)):
        if((i%3 == 0) and (i != 0)):
            print("--------------------------------------")
        for j in range(len(board)):
            if((j%3 == 0) and (j != 0)):
                print('|',end=" ")
            print(str(board[i][j])," ", end=" ")
        print("\n")
        

def findEmptyColumn(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 0):
                return (i,j)
    return None
        
        
def validEntry(board, num, position):
    
    row = position[0]
    column = position[1]
    
    #Check element not in row
    for i in range(len(board)):
        if((board[row][i] == num) and (column != i)):
            return False
    
    #Check element not in column
    for i in range(len(board)):
        if((board[i][column] == num) and (row != i)):
            return False
    
    #Check element not in box
    box_x = column // 3
    box_y = row // 3
    
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if((board[i][j] == num) and ((i,j)!=position)):
                return False
    
    return True


def sudokuSolver(board):
    empty_column = findEmptyColumn(board)
    
    if (empty_column == None):
        return True
    else:
        row, column = empty_column
    
    for entry in range(1,10):
        if(validEntry(board, entry, (row, column))):
            board[row][column] = entry
            
            if(sudokuSolver(board)):
                return True
            
            board[row][column] = 0
    
    return False


if __name__ == '__main__':
    
    initial_board = [
       [2,0,0,0,0,0,0,6,0],
       [0,0,0,0,7,5,0,3,0],
       [0,4,8,0,9,0,1,0,0],
       [0,0,0,3,0,0,0,0,0],
       [3,0,0,0,1,0,0,0,9],
       [0,0,0,0,0,8,0,0,0],
       [0,0,1,0,2,0,5,7,0],
       [0,8,0,7,3,0,0,0,0],
       [0,9,0,0,0,0,0,0,4]
    ]
    
    printBoard(initial_board)
    print("\n")
    sudokuSolver(initial_board)
    print("Solved Sudoku\n")
    printBoard(initial_board)
