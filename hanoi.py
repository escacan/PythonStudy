# 1. check how many blocks are on the position -> n
# 2. move n-1 blocks to aux column & move nth block to dest column.
# 3. move n-1 blocks from aux to dest column.

def hanoi(n, start, dest, aux):
	count= 0
	if n == 1:
		print("move %s"%(start[ len(start) - 1 ]))
		dest.append(start.pop())
		print("start : %s, dest : %s"%(start, dest))
		count += 1
	else:
		count += hanoi(n-1, start, aux, dest)
		print("move %s"%(start[ len(start) - 1 ]))
		dest.append(start.pop())
		print("start : %s, dest : %s"%(start, dest))
		count += 1
		count += hanoi(n-1, aux, dest, start) 
	return count

block_num = int(input())
col_1 = list(range(block_num, 0, -1))
col_2 = []
col_3 = []

print(col_1)
ans= hanoi(block_num, col_1, col_2, col_3)
print("answer : %d"%ans)
