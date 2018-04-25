def block_down(board, y, x):
	if y > 0:
		if board[y][x] is " ":
			temp_y= y-1
			while temp_y >= 0:
				if board[temp_y][x] != " ":
					board[y][x]= board[temp_y][x]
					board[temp_y][x]= " "
					break
				else:
					temp_y -= 1
		block_down(board, y-1, x)

def remove_block(board, remove_li, m):
	for item in remove_li:
		print("On remove block ", item)
		x= item[1]
		y= item[0]
		board[y][x]= " "
		board[y][x+1]= " "
		board[y+1][x]= " "
		board[y+1][x+1]= " "

def check_board(board, m, n):	
	remove_li= []
	for y in range(m-1):
		for x in range(n-1):
			if board[y][x] == board[y][x+1] and board[y][x]== board[y+1][x] \
			   and board[y][x] == board[y+1][x+1] and board[y][x] != " ":
				remove_li.append([y, x])
	if len(remove_li) is 0:
		check_empty= 0
		for y in range(m):
			for x in range(n):
				if board[y][x] == " ":
					check_empty += 1
		print(check_empty)
		return 0
	else:
		remove_block(board, remove_li, m)
		print("After remove,")
		print(board)
		for x in range(n):
			block_down(board, m-1, x)		
		print("After block down,")
		print(board)
		return 1

m= 6
n= 6
board= ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	
print(board)
for i in range(len(board)):
	board[i] = list(board[i])

res= 1
while res== 1:
	res= check_board(board, m, n)	
