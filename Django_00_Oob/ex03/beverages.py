
class HotBeverage:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"
	
	def description(self):
		return "Just some hot water in a cup."
	
	def __str__(self):
		content = f"name : {self.name}\n"
		content += f"price : {self.price}\n"
		content += f"description : {self.description()}"
		return content


class Coffee(HotBeverage):
	def __init__(self):
		super().__init__()
		self.price = 0.40
		self.name = "coffee"
	
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		super().__init__()
		self.price = 0.30
		self.name = "tea"
	
	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__()
		self.price = 0.50
		self.name = "chocolate"

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__()
		self.price = 0.45
		self.name = "cappuccino"

	def description(self):
		return "Un po' di Italia nella sua tazza!"



# if __name__ == '__main__':
# 	baseClass = HotBeverage()
	
# 	coffee = Coffee()
# 	tea = Tea()
# 	chocolate = Chocolate()
# 	cappuccino = Cappuccino()

# 	print(baseClass, end="\n\n")
# 	print(coffee, end="\n\n")
# 	print(tea, end="\n\n")
# 	print(chocolate, end="\n\n")
# 	print(cappuccino)

