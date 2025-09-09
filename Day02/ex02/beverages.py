class HotBeverage:
	price : float = 0.30
	name : str = "hot beverage"

	def	description(self):
		return "Just some hot water in a cup."
	
	def	__str__(self):
		price = "%.2f" % self.price
		return f"name : {self.name}\nprice : {price}\ndescription : {self.description()}"

class Coffee(HotBeverage):
	price : float = 0.40
	name : str = "coffee"

	def	description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	name : str = "tea"

class Chocolate(HotBeverage):
	price : float = 0.50
	name : str = "chocolate"

	def	description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	price : float = 0.45
	name : str = "cappuccino"

	def	description(self):
		return "Un po' di Italia nella sua tazza!"

if __name__ == "__main__" :
	print(HotBeverage(), '\n')
	print(Coffee(), '\n')
	print(Tea(), '\n')
	print(Chocolate(),'\n')
	print(Cappuccino(), '\n')