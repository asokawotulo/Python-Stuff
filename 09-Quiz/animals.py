class animalia():
	def __init__(self, breed, price, age, color, life_span):
		self.breed = breed
		self.price = price
		self.age = age
		self.color = color
		self.life_span = life_span

	def get_breed(self): 
		return self.breed

	def get_price(self): 
		return self.price

	def get_breed_price(self): 
		return self.breed
		return self.price

	def get_info(self):
		print("Breed: " + self.breed)
		print("Price: " + self.price)
		print("Age: " + self.age)
		print("Color: " + self.color)
		print("Life Span: " + self.life_span)