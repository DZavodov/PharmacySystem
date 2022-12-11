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

	def Search(this, name = "", manufacturer = "", country = "", priceMin = 0, priceMax = maxsize):
		"""
		"""

		searchProducts:list[Product] = []
		storageIterator = this.storage.CreateIterator(name, manufacturer, country, priceMin, priceMax)
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
	
	windows = Tk()
	windows.geometry('1000x600')
	
	frame = Frame(windows, padx=5, pady=5)
	frame.grid(row=0, column=1)
	Label(frame, text='Pharmacy System', padx=5, pady=5).pack()
	
	frame1 = Frame(windows, padx=5, pady=5)
	frame1.grid(row=2, column=0)
	
	rows = 5
	columns = 5
	for i in range(rows):
		for j in range(columns):
			Label(frame1, text=f'{i} {j}', padx=5, pady=5, fg='red', bg='yellow', 
				width=15, height=2).grid(row=i, column=j, sticky="we")
			if j == 4:
				Button(frame1, text=f'{i} {j}', padx=5, pady=5, width=15, height=2).grid(row=i, column=j)
		#windows.grid_columnconfigure(i, minsize=400)
	
	#Label(frame1, text='Name', padx=5, pady=5).pack()
	#Label(frame1, text='Email', padx=5, pady=5).pack()
	#Label(frame1, text='Password', padx=5, pady=5).pack()
	
	frame2 = Frame(windows, padx=5, pady=5)
	frame2.grid(row=2, column=1)
	
	#for i in range(rows):
	#	for j in range(1):
	#		Button(frame2, text='{i} {j}', padx=5, pady=5, width=15, height=2).grid(row=i, column=j)
	
	mainloop()
