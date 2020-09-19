from django.http import HttpResponse 
from django.shortcuts import render
import os
import sqlite3


def home_page(request):
	return render(request, 'home_page.html', {'greeting' : 'Welcome to Product Data Base'})

def add_product(request):
	return render(request, 'add_product.html', {'add_item' : 'Add Product'})

def get_product(request):
	return render(request, 'get_product.html', {'get_item' : 'Chose the option for searching please: '})

def confirm(request):
	product_name = request.GET['product_name']
	product_price = request.GET['product_price']
	x = 1
	if x == 1:
		conn = sqlite3.connect("products_db_web.db")
		cursor = conn.cursor()
		# cursor.execute("CREATE TABLE products(product_name TEXT, product_price TEXT);")
		insert_query = f"INSERT INTO products VALUES (?, ?);"
		cursor.execute(insert_query, (str(product_name), float(product_price)))
		conn.commit()
		conn.close()

	
	return render(request, 'confirm.html', {
		'confirm' : 'This product: ',
		'product_name' : product_name,
		'product_price' : product_price,
		})
def result(request):
	product_name_finded = request.GET['product_name_finded']
	product_price_finded = request.GET['product_price_finded']
	x = 1
	if x == 1:
		conn = sqlite3.connect("products_db_web.db")
		cursor = conn.cursor()
		select_query = f"SELECT product_name,product_price FROM products WHERE product_name IS (?) OR product_price IS(?);"
		cursor.execute(select_query,(product_name_finded, product_price_finded))
		result_of_search = cursor.fetchallx()
		conn.commit()
		conn.close()


	return render(request, 'result.html', {
		'result' : 'This result: ',
		'result_of_search' : result_of_search,
		}) 

#, (str(product_name), float(product_price)))

 # WHERE (?) LIKE (? %) OR (?) IS (?)





