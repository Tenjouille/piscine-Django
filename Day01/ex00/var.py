def my_var():
	var1 : int = 42
	var2 : str = '42'
	var3 : str = 'quarante-deux'
	var4 : float = 42.0
	var5 : bool = True
	var6 : list = [42]
	var7 : dict = {42: 42}
	var8 : tuple = (42,)
	var9 : set = set()
	
	print(f"{var1} est de type {type(var1)}")
	print(f"{var2} est de type {type(var2)}")
	print(f"{var3} est de type {type(var3)}")
	print(f"{var4} est de type {type(var4)}")
	print(f"{var5} est de type {type(var5)}")
	print(f"{var6} est de type {type(var6)}")
	print(f"{var7} est de type {type(var7)}")
	print(f"{var8} est de type {type(var8)}")
	print(f"{var9} est de type {type(var9)}")

if __name__ == '__main__':
	my_var()