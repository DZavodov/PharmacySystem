# Copyright 2022 DZavodov. All Rights Reserved.

class Product:
	"""
	"""
	
	def __init__(this, name: str, manufacturer:str, country:str, price: int):
		"""
		"""

		this.name = name
		"""
		"""
		this.manufacturer = manufacturer
		"""
		"""
		this.country = country
		"""
		"""
		this.price = price
		"""
		"""

class StorageIterator:
	"""
	"""
	
	def __init__(this, products: list[Product], name:str, manufacturer:str, country:str):
		"""
		"""

		this.__products = products
		"""
		"""
		this.__index = 0
		"""
		"""
		this.__name = name
		"""
		"""
		this.__manufacturer = manufacturer
		"""
		"""
		this.__country = country
		"""
		"""

	def GoToNext(this):
		"""
		"""

		while this.__index < len(this.__products):

			product = this.__products[this.__index]
			this.__index += 1

			if this.__name in product.name and this.__manufacturer in product.manufacturer and this.__country in product.country:
				return product

		return None

	def GetElement(this):
		"""
		"""

		return this.__products[this.__index]

class StorageSystem:
	"""
	"""
	
	def __init__(this):
		"""
		"""

		this.__products:list[Product] = []
		"""
		"""

	def AddProduct(this, value):
		"""
		"""

		this.__products.append(value)

	def CreateIterator(this, name = "", manufacturer = "", country = ""):
		"""
		"""
		return StorageIterator(this.__products, name, manufacturer, country)

class PaymentSystem:
	"""
	"""

	def __init__(this):
		"""
		"""

		this.__money = 0
		"""
		"""

	def GetMoney(this):
		"""
		"""

		return this.__money

class Facade:
	"""
	Facade
	"""

	def __init__(this, storage:StorageSystem, payment:PaymentSystem):
		"""
		"""

		this.__storage = storage
		"""
		"""
		this.__payment = payment
		"""
		"""

if __name__ == "__main__":
	storage = StorageSystem()
	storage.AddProduct(Product("None0", "None0", "None0", 0))
	storage.AddProduct(Product("None0", "None0", "None1", 1))
	storage.AddProduct(Product("None0", "None1", "None1", 2))
	storage.AddProduct(Product("None1", "None1", "None1", 3))

	storageIterator = storage.CreateIterator(name = "None")
	while storageIterator.GoToNext():
		print(storageIterator.GetElement())

	payment = PaymentSystem()

	facade = Facade(storage, payment)
