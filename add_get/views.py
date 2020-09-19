from django.http import HttpResponse 
from django.shortcuts import render 


def home_page(request):
	return render(request, 'home_page.html', {'greeting' : 'Welcome to Product Data Base'})

def add_product(request):
	return render(request, 'add_product.html', {'add_item' : 'Add Product'})

def get_product(request):
	return render(request, 'get_product.html', {'get_item' : 'Get Product'})
def confirm(request):
	product_name = request.GET['product_name']
	product_price = request.GET['product_price']
	return render(request, 'confirm.html', {
		'confirm' : 'This product: ',
		'product_name' : product_name,
		'product_price' : product_price,
		})
		