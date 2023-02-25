from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Feedback, Product, Filter, Customer


class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['author', 'text']

		widgets = {
			'author':TextInput(attrs={
				'class':'author',
				'placeholder':'Your Name'
			}),
			'text':Textarea(attrs={
				'class':'feedback',
				'placeholder':'Your Feedback'
				}),
		}

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['img', 'name', 'price', 'category']

		widgets = {
			'img':TextInput(attrs={
				'class':'img',
				'placeholder':'Product Image Link'
				}),
			'name':TextInput(attrs={
				'class':'name',
				'placeholder':'Product Name'
				}),
			'price':NumberInput(attrs={
				'class':'price',
				'placeholder':'Product Price (UZS)'
				}),
		}

class FilterForm(ModelForm):
	class Meta:
		model = Filter
		fields = ['name']

		widgets = {
			'name':TextInput(attrs={
				'class':'add_filter',
				'name':'add_category',
				'placeholder':'Add New Category'
				})
		}

class DelFilterForm(ModelForm):
	class Meta:
		model = Filter
		fields = ['name']

class EditProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

		widgets = {
			'img':TextInput(attrs={
				'class':'img',
				'placeholder':'Product Image Link'
				}),
			'name':TextInput(attrs={
				'class':'name',
				'placeholder':'Product Name'
				}),
			'price':NumberInput(attrs={
				'class':'price',
				'placeholder':'Product Price (UZS)'
				}),
		}

class EditCategoryForm(ModelForm):
	class Meta:
		model = Filter
		fields = '__all__'

		widgets = {
			'name':TextInput(attrs={
				'class':'name',
				'placeholder':'Category Name'
				}),
		}

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

		widgets = {
			'name':TextInput(attrs={
				'class':'customer',
				'placeholder':'Your Name'
				}),
			'phone':NumberInput(attrs={
				'class':'phone',
				'placeholder':'Your Phone Number'
				}),
			'addres':TextInput(attrs={
				'class':'addres',
				'placeholder':'Your Addres'
				}),
		}