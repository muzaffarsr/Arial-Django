from django.db import models


class Filter(models.Model):
	name = models.CharField('Filter Name', max_length=10)

	def __str__(self):
		return self.name

class Product(models.Model):
	img = models.TextField('Product Image Link')
	name = models.CharField('Product Name', max_length=15)
	price = models.PositiveIntegerField('Product Price (UZS)')
	category = models.ForeignKey(Filter, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category
	def __str__(self):
		return self.price
	def __str__(self):
		return self.name

class Feedback(models.Model):
	author = models.CharField('Feedback Author', max_length=50)
	text = models.TextField('Feedback')
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.author
	def __str__(self):
		return self.pub_date
	def __str__(self):
		return self.text

class Customer(models.Model):
	name = models.CharField('Customer Name', max_length=50)
	phone = models.PositiveIntegerField('Customer Phone Number')
	addres = models.TextField('Customer Addres')
	product = models.PositiveIntegerField()
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.phone
	def __str__(self):
		return self.pub_date
	def __str__(self):
		return self.addres
	def __str__(self):
		return self.name