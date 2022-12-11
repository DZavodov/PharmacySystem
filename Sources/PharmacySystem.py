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
	searchProductsFrame.grid(row=1)

	def CreateLabel(root:Misc, row:int, column:int, text:str):
		"""
		"""

		Label(root, text = text, padx=5, pady=5, fg='red', bg='yellow', width=15, height=0).grid(row=row, column=column, sticky="we")

	def CreateButton(root:Misc, text:str, command):
		"""
		"""

		return Button(root, text=text, command=command, padx=5, pady=5, width=15, height=0)

	def CreateProduct(root:Misc, index:int, product:Product, buttonText:str, buttonCommand):
		"""
		"""

		CreateLabel(root, index, 0, product.name)
		CreateLabel(root, index, 1, product.manufacturer)
		CreateLabel(root, index, 2, product.country)
		CreateLabel(root, index, 3, product.price)

		CreateButton(root, buttonText, buttonCommand).grid(row=index, column=4)

	CreateLabel(searchProductsFrame, 0, 0, "Наименование")
	CreateLabel(searchProductsFrame, 0, 1, "Производитель")
	CreateLabel(searchProductsFrame, 0, 2, "Страна")
	CreateLabel(searchProductsFrame, 0, 3, "Цена")

	Entry(searchProductsFrame).grid(row=1, column=0, sticky="we")
	Entry(searchProductsFrame).grid(row=1, column=1, sticky="we")
	Entry(searchProductsFrame).grid(row=1, column=2, sticky="we")
	Entry(searchProductsFrame).grid(row=1, column=3, sticky="we")

	def UpdateSearchProducts():
		"""
		"""

		for index in range(len(searchProductsFrame.winfo_children()) - 9):
			searchProductsFrame.winfo_children().pop().destroy()

		products = facade.Search(name = "None", limit = 10)
		for index in range(len(products)):
			CreateProduct(searchProductsFrame, index + 2, products[index], ">", None)

	CreateButton(searchProductsFrame, "Найти", None).grid(row=1, column=4)

	UpdateSearchProducts()

	basketProductsFrame = Frame(windows, padx=5, pady=5)
	basketProductsFrame.grid(row=1, column=2)

	facade.basketProducts.append(Product("None","None","None",0))
	facade.basketProducts.append(Product("None","None","None",0))
	facade.basketProducts.append(Product("None","None","None",0))
	facade.basketProducts.append(Product("None","None","None",0))

	CreateLabel(basketProductsFrame, 0, 0, "Наименование")
	CreateLabel(basketProductsFrame, 0, 1, "Производитель")
	CreateLabel(basketProductsFrame, 0, 2, "Страна")
	CreateLabel(basketProductsFrame, 0, 3, "Цена")

	def DeleteBasketProduct(index:int):
		"""
		"""

		facade.basketProducts.pop(index)

		UpdateBasketProducts()

	def UpdateBasketProducts():
		"""
		"""

		for index in range(len(basketProductsFrame.winfo_children()) - 4):
			basketProductsFrame.winfo_children().pop().destroy()

		for index in range(len(facade.basketProducts)):
			CreateProduct(basketProductsFrame, index + 1, facade.basketProducts[index], "X", lambda index=index: DeleteBasketProduct(index))

	UpdateBasketProducts()

	mainloop()
