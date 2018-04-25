'''"
1S2D*3T,
1D2S#10S,
1D2S0T,
1S*2T*3S,
1D#2S*3S,
1T2D3D#,
1D2S3T*
'''

def dart(testcase):
	num= []
	for i in range(11):
		num.append(str(i))
	# print(num)

	score_li= []

	temp_num= None
	for i in range(len(testcase)):
		# str[i] is in num, temp_num is -1
		# print(testcase[i])
		if testcase[i] in num:
			if temp_num is None:
				# temp_num= int(str[i])
				temp_num= int(testcase[i])
			# str[i] is in num, temp_num is not -1
			else:
				# 	str[i] is "0", temp_num *= 10
				if int(testcase[i]) is 0 and temp_num is 1:
					temp_num *= 10
				# 	str[i] is not "0", score_li.append(temp_num) & temp_num= int(str[i])
				else:
					score_li.append(temp_num)
					temp_num = int(testcase[i])
		# if str[i] is S temp_num**1  D temp_num**2  T temp_num**3
		elif testcase[i] is "S":
			temp_num= temp_num
		elif testcase[i] is "D":
			temp_num= temp_num* temp_num
		elif testcase[i] is "T":
			temp_num= temp_num* temp_num * temp_num
		# if str[i] is *
		elif testcase[i] is "*":
		# if score_li is empty-> temp_num *= 2 
			if not len(score_li):
				temp_num *= 2
		# else score_li[-1] *= 2 & temp_num *= 2
			else:
				score_li[-1] *= 2
				temp_num *= 2
		# if testcase[i] is #      temp_num *= -1
		else:
			temp_num *= -1
		# print(temp_num)
		if i == len(testcase) - 1:
			score_li.append(temp_num)
		# print(score_li)
	print("ans: ", score_li[0] + score_li[1] + score_li[2])

testcase= [
	"10S2D*3T",
	"1D2S#10S",
	"1D2S0T",
	"1S*2T*3S",
	"1D#2S*3S",
	"1T2D3D#",
	"1D2S3T*"
]
for res in testcase:
	print("question : ", res)
	dart(res)