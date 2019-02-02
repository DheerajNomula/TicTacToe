# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:47:49 2018

@author: Nomula Dheeraj Kumar
"""
from goto import goto, label

print('Choose between "X" and "O"')
player=input()
if(player=='X'):
   computer='O'
   current=player
else:
   computer='X'
   current=computer
   

   
def is_full(board):
	for i in range(3):
		for j in range(3):
			if(board[i][j]==' '):
				return False
	return True
	
	
def evaluate(board):
	win_state = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
	
	if([player,player,player] in win_state):
		return 10
	elif([computer,computer,computer] in win_state):
		return -10
	return 0


def minimax(board,depth,maximising):
	score=evaluate(board)                                                                  
	
	if(score==10):
		return score
	
	if(score==-10):
		return score
	
	if(is_full(board)):
		return 0
	
	if(maximising==True):
		best=-1000
		for i in range(3):
			for j in range(3):
				if(board[i][j]==' '):
					board[i][j]=player
					best=max(best,minimax(board,depth+1,False))
					board[i][j]=' '
		return best-depth
	else:
		best=1000
		for i in range(3):
			for j in range(3):
				if(board[i][j]==' '):
					board[i][j]=computer
					best=min(best,minimax(board,depth+1,True))
					board[i][j]=' '
		return best+depth

def display(board):
	for i in range(3):
			for j in range(3):
				temp=board[i][j]
				if(temp==' '):
					temp='-'
				print(temp,end=' ')
			print('\n')

def find_best_move(board):
	
	best=1000
	row=-1
	col=-1
	for i in range(3):
		for j in range(3):
			if(board[i][j]!=' '):
				continue
			board[i][j]=computer
			temp=minimax(board,1,True)
			print('i= ',i,' j= ',j,' value= ',temp)
			if(temp<best):
				row=i
				col=j
				best=temp
			board[i][j]=' '
	print('row= ',row,' col= ',col)
	board[row][col]=computer


board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print('Initial board structure' )
display(board)
i=0
while(True):
	i+=1
	print(i)
	cost=evaluate(board)
	if(cost==10):
		print(player,' is the WINNER !! GAME ENDS')
		break
	elif(cost==-10):
		print(computer,' is the WINNER!! GAME ENDS')
		break
	if(is_full(board)):
		print('TIE !! GAME ENDS')
		break

	if(current==player):
		label .here
		print('Enter the location(Starts indexing from 0)....')
		print('Enter the row to be choosen :-')
		x=int(input())
		print('Enter the column to be choosen :-')
		y=int(input())
		if(board[x][y]!=' '):
			print('This position is already taken !!! Choose another position....')
			goto .here
		board[x][y]=player
		current=computer
	else:
		find_best_move(board)
		current=player
	display(board)
	
	
	
