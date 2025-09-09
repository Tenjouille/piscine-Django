import beverages
import random

class   CoffeeMachine:
	def __init__(self):
		return
	
	state = True
	count = 0

	class   EmptyCup(beverages.HotBeverage):
		name : str = "empty cup"
		price : float = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		if self.state == True:
			print("Stop calling the tech guy, the machine is not broken !", '\n')
		else:
			self.state = True
			print("The coffee machine is working again (not under guarentee though...)", '\n')
	
	def serve(self, bev):
		if self.state == False:
			raise self.BrokenMachineException()
		rand = random.randint(0, 1)
		if rand == 0:
			bev = self.EmptyCup()
		self.count += 1
		if self.count >= 10:
			self.count = 0
			self.state = False
		return bev

if __name__ == "__main__" :
	coffeeMachine = CoffeeMachine()
	coffee = beverages.Coffee()
	tea = beverages.Tea()
	choco = beverages.Chocolate()
	cappu = beverages.Cappuccino()

	for i in range(6):
		try:
			print(coffeeMachine.serve(coffee), '\n')
			print(coffeeMachine.serve(tea), '\n')
			print(coffeeMachine.serve(choco), '\n')
			print(coffeeMachine.serve(cappu), '\n')
			coffeeMachine.repair()
		except coffeeMachine.BrokenMachineException:
			coffeeMachine.repair()
		print(coffeeMachine.serve(beverages.HotBeverage), '\n')