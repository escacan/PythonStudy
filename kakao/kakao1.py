# 5
# 9
# 20
# 28
# 18
# 11
# 30
# 1
# 21
# 17
# 28

# N = int(input())
# N= 5
# arr1= [9,20,28,18,11]
# arr2= [30,1,21,17,28]

N= 6
arr1= [46,33, 33, 22, 31, 50]
arr2= [27,56, 19, 14, 14, 10]


ans= []

# for i in range(N):
# 	temp= int(input())
# 	arr1.append(temp)
# for i in range(N):
# 	temp= int(input())
# 	arr2.append(temp)

# print(arr1, arr2)

for i in range(N):
	decode1= []
	num= arr1[i]
	while num != 1:
		decode1.append(int(num % 2))
		num = int(num / 2)
	decode1.append(1)
	while len(decode1) < N:
		decode1.append(0)
	# print(decode1)
	arr1[i]= decode1

for i in range(N):
	decode2= []
	num= arr2[i]
	while num != 1:
		decode2.append(int(num % 2))
		num = int(num / 2)
	decode2.append(1)
	while len(decode2) < N:
		decode2.append(0)
	# print(decode2)
	arr2[i]= decode2


# print(arr1)
# print(arr2)

for i in range(N):
	temp= ""
	for j in range(N):
		# print(i, j)
		# print( (arr1[i][j] | arr2[i][j]) )
		if (arr1[i][j] | arr2[i][j]):
			temp= "#" + temp
		else:
			temp= " " + temp
		# print(temp)
	ans.append(temp)
print(ans)