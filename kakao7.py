def compare_time(t1, t2):
	if t1[0] > t2[0]:
		return False
	elif t1[0] < t2[0]:
		return True
	else:
		if t1[1] > t2[1]:
			return False
		elif t1[1] < t2[1]:
			return True
		else:
			if t1[2] >= t2[2]:
				return False
			else:
				return True


def check_start_time(t1):
	temp_hour= t1[0]
	temp_min= t1[1]
	temp_sec= t1[2]
	T = t1[3]

	if temp_sec < T:
		if temp_min == 0:
			temp_hour -= 1
			temp_min = 59
			temp_sec = temp_sec + 60 - T
		else:
			temp_min -= 1
			temp_sec = temp_sec + 60 - T
	else:
		temp_sec -= T
	start_time= [temp_hour, temp_min, temp_sec]
	return start_time

# arguments are end_time 
def check_time_gap(interval_time, target_time):
	target_start_time = check_start_time(target_time)
	interval_start_time = check_start_time(interval_time)

	if compare_time(target_start_time, interval_start_time):
		if compare_time(target_time, interval_start_time):
			return False
		else:
			return True
	elif compare_time(interval_time, target_start_time):
		return False
	else:
		return True


li= ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
for i in range(len(li)):
	end_time= []
	item= li[i]
	item= item[item.index(" ") + 1:]
	end_time.append(int(item[:2]))
	end_time.append(int(item[3:5]))
	end_time.append(float(item[6:12]))
	end_time.append(float(item[13:-1]))
	li[i]= end_time

print(li)
