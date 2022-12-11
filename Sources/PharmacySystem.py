# Copyright 2022 DZavodov. All Rights Reserved.

from sys import maxsize
from tkinter import *
from tkinter import ttk

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
	
	def __init__(this, products: list[Product], name:str, manufacturer:str, country:str, priceMin:int, priceMax:int):
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
		this.__priceMin = priceMin
		"""
		"""
		this.__priceMax = priceMax
		"""
		"""

	def GoToNext(this):
		"""
		"""

		while this.__index < len(this.__products) - 1:

			this.__index += 1
			product = this.__products[this.__index]

			if this.__name in product.name and this.__manufacturer in product.manufacturer and this.__country in product.country and product.price >= this.__priceMin and product.price <= this.__priceMax:
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

	def CreateIterator(this, name:str, manufacturer:str, country:str, priceMin:int, priceMax:int):
		"""
		"""
		return ProductIterator(this.__products, name, manufacturer, country, priceMin, priceMax)

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

	def Search(this, name = "", manufacturer = "", country = "", priceMin = 0, priceMax = maxsize, limit = maxsize):
		"""
		"""

		searchProducts:list[Product] = []
		storageIterator = this.storage.CreateIterator(name, manufacturer, country, priceMin, priceMax)
		while storageIterator.GoToNext():
			searchProducts.append(storageIterator.GetCurrent())
			if len(searchProducts) >= limit:
				break

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
	facade.storage.AddProduct(Product("None2", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None3", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None4", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None5", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None6", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None7", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None8", "None1", "None1", 3))
	facade.storage.AddProduct(Product("None9", "None1", "None1", 3))

	# View
	windows = Tk()
	windows.geometry('1000x600')

	headerFrame = Frame(windows, padx=5, pady=5)
	headerFrame.grid(row=0, column=1)
	Label(headerFrame, text='Pharmacy System', padx=5, pady=5).pack()

	searchProductsFrame = Frame(windows, padx=5, pady=5)
	searchProductsFrame.grid(row=2, column=0)

	name = ""
	def Search():
		"""
		"""

		for widget in searchProductsFrame.winfo_children():
			widget.destroy()

		products = facade.Search(name = name, limit = 10)

		def CreateColumn(index:int, column:int, text:str):
			"""
			"""
			Label(searchProductsFrame, text = text, padx=5, pady=5, fg='red', bg='yellow', width=15, height=2).grid(row=index, column=column, sticky="we")

		def CreateRow(index:int, product:Product):
			"""
			"""

			CreateColumn(index, 0, product.name)
			CreateColumn(index, 1, product.manufacturer)
			CreateColumn(index, 2, product.country)
			CreateColumn(index, 3, product.price)
			
			Button(searchProductsFrame, text = "->", padx=5, pady=5, width=15, height=2).grid(row=index, column=4)

		CreateColumn(0, 0, "Наименование")
		CreateColumn(0, 1, "Производитель")
		CreateColumn(0, 2, "Страна")
		CreateColumn(0, 3, "Цена")

		for index in range(1, len(products) + 1):
			CreateRow(index, products[index - 1])

	name = "None"
	Search()
	name = "None0"
	Search()

	mainloop()
