from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
	def __init__(self):
		self.uses = 0
	class EmptyCup(HotBeverage):
		def __init__(self):
			super().__init__()
			self.price = 0.90
			self.name = "empty cup"

		def description(self):
			return "An empty cup?! Gimme my money back!"
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	def repair(self):
		self.uses = 0
	def serve(self, derivedClass):
		if not issubclass(derivedClass, HotBeverage):
			raise TypeError("derivedClass must be a subclass of HotBeverage")
		if self.uses >= 10:
			raise self.BrokenMachineException()
		if random.randint(0, 1):
			return self.EmptyCup()
		else:
			self.uses += 1
			return derivedClass()
		

if __name__ == '__main__':
	coffee_machine = CoffeeMachine()
	
	random_choice = random.randrange(0, 2)
	drinks = [Coffee, Tea, Chocolate, Cappuccino]
	
	nbr_of_drinks = 20
	for i in range(nbr_of_drinks):
		try:
			print(f"---------------drink nbr {i}----------------")
			print(CoffeeMachine.serve(coffee_machine, drinks[random_choice]), end="\n\n")
			random_choice = random.randrange(0, 2)
		except Exception as e:
			print(f"---------------machine is broken----------------")
			print(e)
			coffee_machine.repair()
			print("Machine repaired.", end="\n\n")
			print(CoffeeMachine.serve(coffee_machine, drinks[random_choice]), end="\n\n")