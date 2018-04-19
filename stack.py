class Stack:
	def __init__(self):
		self.data= []
	def push(self, newdata):
		self.data.append(newdata)
	def pop(self):
		self.data.pop()
	def peek(self):
		if not self.data.isempty():
			return self.data[ len(self.data) - 1 ]
		else:
			return "empty"
	def size(self):
		return len(self.data)

def checkB():
	stk= Stack()
	ques = input()
	for i in range(len(ques)):
		if ques[i] == '(':
			stk.push('(')
		elif ques[i] == '[':
			stk.push('[')
		elif ques[i] == '{':
			stk.push('{')
		elif ques[i] == ')':
			if stk.peek() == '(':
				stk.pop()
			else:
				return "unbalanced"
		elif ques[i] == ']':
			if stk.peek() == '[':
				stk.pop()
			else:
				return "unbalanced"
		elif ques[i] == '}':
			if stk.peek() == '{':
				stk.pop()
			else:
				return "unbalanced"
	
	if stk.size() != 0:
		return "unbalanced"
	else:
		return "balanced"

res= checkB()
print(res)
