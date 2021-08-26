class CalcSolver:
	eq = ''
	operationsAllowed = ['+', '-', '*', '/']

	def __init__(self, equation):
		self.eq = equation

	def addition(self, a, b):
		return a + b

	def subtration(self, a, b):
		return a - b

	def multiplication(self, a, b):
		return a * b

	def division(self, a, b):
		return a / b

	def simplify(self):
		self.eq = self.eq.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+')

	def splitString(self):
		pieces = []
		lastSplitted = 0
		aux = ''

		for i in self.eq:
			if i in self.operationsAllowed:
				if aux != '':
					pieces.append(aux)
					aux = ''
				pieces.append(i)
			else:
				aux += i

		if aux != '':
			pieces.append(aux)

		return pieces

	def calcSplits(self, splitted):
		result = None

		for i, e in enumerate(splitted):
			if e in self.operationsAllowed:
				if e == '+' and ('*' not in splitted and '/' not in splitted):
					if i != 0:
						result = self.addition(int(splitted[i-1]), int(splitted[i+1]))
					else:
						result = splitted[i] + splitted[i+1]
				elif e == '-' and ('*' not in splitted and '/' not in splitted):
					if i != 0:
						result = self.subtration(int(splitted[i-1]), int(splitted[i+1]))
					else:
						result = splitted[i] + splitted[i+1]
				elif e == '*':
					result = self.multiplication(int(splitted[i-1]), int(splitted[i+1]))
				elif e == '/':
					result = self.division(int(splitted[i-1]), int(splitted[i+1]))

				if result != None:
					splitted[i] = result
					if i > 0:
						splitted.pop(i+1)
						splitted.pop(i-1)
					else:
						splitted.pop(i+1)

					return self.calcSplits(splitted)

		return splitted

	def solve(self):
		self.simplify()
		splitted = self.splitString()
		r = self.calcSplits(splitted)
		
		return splitted