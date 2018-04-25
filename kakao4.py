'''
n : how many bus
t : interval
m : max on each bus
timetable= ["HH:MM", ... ]
'''
# n = 1
# t = 1
# m = 5
# timetable= ["08:00", "08:01", "08:02", "08:03"]

n = 10
t = 60
m = 45
timetable= ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

# 2	1	2	["09:00", "09:00", "09:00", "09:00"]

# Check when the bus arrive

bus_li= []
crew_count= []

for i in range(n):
	# check interval & add item on bus_li
	temp_time = t * i
	temp_hour= 9 + int(temp_time / 60)
	temp_min = temp_time % 60
	next_time= temp_hour * 100 + temp_min

	bus_li.append(next_time)

print(bus_li)

print(timetable)

for i in range(len(timetable)):
	item= timetable[i]
	item= int(item.replace(":", ""))
	timetable[i] = item

timetable.sort()
print(timetable)

cur_li= 0
for i in range(len(bus_li)):
	crew_count.append(0)

# for i in range(len(timetable)):
i= 0
while i < len(timetable):	
	if timetable[i] <= bus_li[cur_li]:
		crew_count[cur_li] += 1
		i += 1
	else:
		cur_li += 1
		if cur_li >= n:
			break
		crew_count[cur_li] = crew_count[cur_li - 1]

print(crew_count)

if crew_count[-1] <= n* m - 1:
	temp_val= 0
	if n > 1:
		temp_val= crew_count[-1] - crew_count[-2]		
	else:
		temp_val= crew_count[0]

	if temp_val < m:
		if bus_li[-1] < 1000:
			print("%d:%d"%(int(bus_li[-1] / 100), bus_li[-1] % 100 ))
		else:
			print("%d:%d"%(int(bus_li[-1] / 100), bus_li[-1] % 100 ))
	else:
		if n > 1:
			last_crew= timetable[crew_count[-2] + m - 1]
		else:
			last_crew= timetable[m - 1]

		if last_crew % 100 is 0:
			last_crew = last_crew - 100 + 59
		else:
			last_crew -= 1

		if last_crew < 1000:
			print("%d:%d"%(int(last_crew / 100), last_crew % 100 ))
		else:
			print("%d:%d"%(int(last_crew / 100), last_crew % 100 ))
else:
	last_crew= timetable[crew_count[-1] - n * m + 1]
	print(last_crew)
	if last_crew % 100 is 0:
		last_crew = last_crew - 100 + 59
	else:
		last_crew -= 1

	if last_crew < 1000:
		print("%d:%d"%(int(last_crew / 100), last_crew % 100 ))
	else:
		print("%d:%d"%(int(last_crew / 100), last_crew % 100 ))