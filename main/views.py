from django.shortcuts import render, redirect
from .models import Product, Filter, Feedback
from .forms import FeedbackForm, ProductForm, FilterForm, DelFilterForm, EditProductForm, EditCategoryForm, CustomerForm

def home(request):
	filters = Filter.objects.all()
	products = Product.objects.order_by('-pub_date')
	return render(request, 'main/index.html', {'filters':filters, 'products':products})

def filter(request, filter):
	filters = Filter.objects.all()
	products = Product.objects.filter( category = filter )
	return render(request, 'main/index.html', {'filters':filters, 'products':products})

def search(request):
	search_text = request.GET.get('search')
	if len(search_text) >= 1:
		filters = Filter.objects.all()
		products = Product.objects.filter( name__icontains = request.GET.get('search') )
		return render(request, 'main/index.html', {'filters':filters, 'products':products})
	else:
		return redirect('home')

def product(request, product_id):
	product = Product.objects.get( id = product_id )
	return render(request, 'main/product.html', {'product':product})

def customer(request, product_id):
	product = Product.objects.get( id = product_id )
	if request.method == 'POST':
		return redirect('home')
	form = CustomerForm()
	return render(request, 'main/customer.html', {'product':product, 'form':form})

def orders(request):
	orders = Customer.objects.order_by('-pub_date')
	return render(request, 'main/orders.html', {'orders':orders})

def del_order(request, order_id):
	order = Customer.objects.get( id = order_id )
	order.delete()
	return redirect('orders')

def leave_feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		form.save()
		return redirect('home')
	form = FeedbackForm()
	return render(request, 'main/leave_feedback.html', {'form':form})

def manage(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid:
			form.save()
		else:
			pass
	total = Product.objects.count()
	form = ProductForm()
	filterForm = FilterForm()
	filters = Filter.objects.all()
	def render_filter(request):
		render_filter = True
		return redirect('manage') 
	products = Product.objects.order_by('-pub_date')
	return render(request, 'main/manage.html', {'form':form, 'filterForm':filterForm, 'total':total, 'products':products, 'filters':filters})

def category(request):
	categorys = Filter.objects.all()
	total = Filter.objects.count()
	return render(request, 'main/categorys.html', {'total':total, 'categorys':categorys})

def feedbacks(request):
	feedbacks = Feedback.objects.order_by('-pub_date')
	return render(request, 'main/feedbacks.html', {'feedbacks':feedbacks})

def add_category(request):
	if request.method == 'POST':
		form = FilterForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('manage')
		else:
			pass

def del_category(request, category_id):
	category = Filter.objects.get( id = category_id )
	category.delete()
	return redirect('category')

def del_product(request, product_id):
	product = Product.objects.get( id = product_id )
	product.delete()
	return redirect('manage')

def del_feedback(request, feedback_id):
	feedback = Feedback.objects.get( id = feedback_id )
	feedback.delete()
	return redirect('feedbacks')

def edit_product(request, product_id):
	product = Product.objects.get( id = product_id )
	if request.method == 'POST':
		formValue = EditProductForm(request.POST, instance=product)
		if formValue.is_valid:
			formValue.save()
			return redirect('manage')
		else:
			pass

	formValue = EditProductForm(instance=product)
	return render(request, 'main/edit-product.html', {'product':product, 'formValue':formValue})

def edit_category(request, category_id):
	category = Filter.objects.get( id = category_id )
	if request.method == 'POST':
		formValue = EditCategoryForm(request.POST, instance=category)
		if formValue.is_valid:
			formValue.save()
			return redirect('category')
		else:
			pass

	formValue = EditCategoryForm(instance=category)
	return render(request, 'main/edit-category.html', {'category':category, 'formValue':formValue})

def error_404(request, exception):
	return render(request, 'err_404.html')