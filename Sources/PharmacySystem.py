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

class ProductIterator:
	"""
	"""
	
	def __init__(this, products: list[Product], name:str, manufacturer:str, country:str):
		"""
		"""

		this.__products = products
		"""
		"""
		this.__index = -1
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

		while this.__index < len(this.__products) - 1:

			this.__index += 1
			product = this.__products[this.__index]

			if this.__name in product.name and this.__manufacturer in product.manufacturer and this.__country in product.country:
				return product

		return None

	def GetCurrent(this):
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

	def CreateIterator(this, name:str, manufacturer:str, country:str):
		"""
		"""
		return ProductIterator(this.__products, name, manufacturer, country)

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

	def DecrementMoney(this, value: int):
		"""
		"""

		this.__money -= value

class Facade:
	"""
	"""

	def __init__(this, storage = StorageSystem(), payment = PaymentSystem()):
		"""
		"""

		this.storage = storage
		"""
		"""
		this.payment = payment
		"""
		"""

		this.basketProducts:list[Product] = []
		"""
		"""

	def Search(this, name = "", manufacturer = "", country = ""):
		"""
		"""

		searchProducts:list[Product] = []
		storageIterator = this.storage.CreateIterator(name, manufacturer, country)
		while storageIterator.GoToNext():
			searchProducts.append(storageIterator.GetCurrent())

		return searchProducts

	def TryBuy(this):
		"""
		"""

		price = 0
		for product in this.basketProducts:
			price += product.price

		if price > this.payment.GetMoney():
			return False

		this.payment.DecrementMoney(price)

		this.basketProducts.clear()

		return True

if __name__ == "__main__":
	facade = Facade()

	facade.storage.AddProduct(Product("None0", "None0", "None0", 0))
	facade.storage.AddProduct(Product("None0", "None0", "None1", 1))
	facade.storage.AddProduct(Product("None0", "None1", "None1", 2))
	facade.storage.AddProduct(Product("None1", "None1", "None1", 3))

	facade.payment.DecrementMoney(-5)

	facade.basketProducts = facade.Search(name = "None0")

	for product in facade.basketProducts:
		print(product.price)
	print(facade.TryBuy())
	print(facade.payment.GetMoney())
