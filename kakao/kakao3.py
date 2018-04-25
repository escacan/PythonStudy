N= 0
total_time= 0
cache= []
# cities= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities= ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

if N is 0:
	total_time= len(cities)*5
else:
	for i in range(len(cities)):
		name = cities[i]
		if name in cache:
			total_time += 1
			cache.remove(name)
			cache.insert(0, name)
		else:
			total_time += 5
			if len(cache) == N:
				cache.pop()
			cache.insert(0, name)

print("answer: ", total_time)	