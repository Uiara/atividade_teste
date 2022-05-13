class Node:
	def __init__(self, data, previous = None, next = None):
		self._data = data 
		self._next = next
		self._previous = previous

	def getData(cls):
		return cls._data

	def setData(cls, newData):
		cls._dado = newData

	def getPrevious(cls):
		return cls._previous

	def setPrevious(cls, newPrevious):
		cls._previous = newPrevious

	def getNext(cls):
		return cls._next

	def setNext(cls, newNext):
		cls._next = newNext


class Pilha:
	def __init__(self, content, start = None, end = None):
		self._start = start
		self._end = end 
		self.content = content 	# Recebe uma lista
	
	def getStart(cls):
		return cls._start

	def setStart(cls, newstart):
		cls._start = newstart

	def getEnd(cls):
		return cls._end

	def setEnd(cls, newEnd):
		cls._end = newEnd

	def isEmpty(cls):
		return (cls.getStart() is None) and (cls.getEnd() is None)

	def insertInEnd(cls):
		for item in cls.content:
			no = Node(item)	# criando um nó com um data específico
			if cls.isEmpty():
				cls.setStart(no)
				cls.setEnd(no)
			else:
				no.setPrevious(cls.getEnd())
				cls.getEnd().setNext(no)
				cls.setEnd(no)

	def removeLast(cls):
		if not cls.isEmpty():
			dataRemoved = cls.getEnd().getData()
			if cls.getStart() == cls.getEnd():
				# Caso a lista só tenha um único elemento.
				cls.setStart(None) 
				cls.setEnd(None)
			else:
				# Caso ela esteja multipopulada.
				cls.setEnd(cls.getEnd().getPrevious())
				cls.getEnd().setPrevious(None)
			return dataRemoved
		else:
			print('Lista vazia, cão!')

	def sweep(cls):
		countParenthesis = 0
		countBrackets = 0
		countKeys = 0

		while not cls.isEmpty() and (countParenthesis >= 0 and countBrackets >= 0 and countKeys >= 0):
			exp = cls.removeLast()
			if exp == ')': 
				countParenthesis += 1
			elif exp == '(':
				countParenthesis -= 1
			elif exp == ']':
				countBrackets += 1
			elif exp == '[':
				countBrackets -= 1
			elif exp == '}':
				countKeys += 1
			elif exp == '{':
				countKeys -= 1

		if countParenthesis == 0 and countBrackets == 0 and countKeys == 0:
			return 'S'
		else:
			return 'N'



verifications = int(input())
listExpressions = []
for i in range(verifications):
	entry = input()
	listExpressions += [entry]
	
for expression in listExpressions:
	pilha = Pilha(expression)
	pilha.insertInEnd()
	print(pilha.sweep())