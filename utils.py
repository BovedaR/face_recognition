class loading_bar:
	def __init__(self, total=100, amount=100):
		self.amount = amount
		self.total = int(total)
		self.completed = 0
	def set(self, num):
		self.completed = num

	def add(self, num):
		self.completed += num

	def __repr__(self):
		if self.completed >= self.total: return f"[{'#'*self.amount}] (100%)"
		return f"[{'#'*int(self.completed*self.amount/self.total)}{'-'*int(self.amount-int(self.completed*self.amount/self.total))}] ({round(self.completed/self.total * 100, 2)}%)"