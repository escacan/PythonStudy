string1= "E=M*C^2"
string2= "e=m*c^2"

alphabet= ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

string1 = string1.upper()
string2 = string2.upper()

decode_str1= []
decode_str2= []

for i in range(len(string1) - 1):
	if string1[i] in alphabet and string1[i+1] in alphabet:
		decode_str1.append(string1[i:i+2])

for i in range(len(string2) - 1):
	if string2[i] in alphabet and string2[i+1] in alphabet:
		decode_str2.append(string2[i:i+2])

set_str1 = set(decode_str1)
set_str2 = set(decode_str2)

print(decode_str1)
print(decode_str2)
print(set_str1)
print(set_str2)

# get | &  result.
sum_set = set_str1 | set_str2
inter_set = set_str1 & set_str2

# get count for each item for each set.
# Based on str1's element,  check count. 
# Min value is go to intersection
min_val= 0
max_val= 0
for item in inter_set:
	if decode_str1.count(item) > decode_str2.count(item):
		min_val += decode_str2.count(item)
	else:
		min_val += decode_str1.count(item)
# Max value go to 
for item in sum_set:
	if decode_str1.count(item) > decode_str2.count(item):
		max_val += decode_str1.count(item)
	else:
		max_val += decode_str2.count(item)

if max_val is 0:
	print(65536)
else:
	print(int(min_val / max_val * 65536))