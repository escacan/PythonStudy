class node(object):
	def __init__(self, data):
		self.data= data
		self.next= None

class linkedlist(object):
	def __init__(self):
		self.head= node(-1)
		self.size= 0
	def add(self, data):
		newNode = node(data)
		self.head.next= newNode
		self.size += 1


list = linkedlist()
print("list size : ", list.size)

list.add(3)
list.add(4)

print("list size : ", list.size)
