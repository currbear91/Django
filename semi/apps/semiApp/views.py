from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def indexs(request):
	print "*" * 50
	# print Product.objects.product_name()
	print "*" * 50
	print Product.objects.all()

	context ={

		"products" : Product.objects.all()
		

	}

	return render(request, 'semiAppTemplates/index.html', context)
	
def shows(request, id):

	context ={

		"products" : Product.objects.get(id = id)
		

	}

	
	return render(request, 'semiAppTemplates/show.html', context)
	
def news(request): #Add New product for

	return render(request, 'semiAppTemplates/new.html')
	
def edits(request, id):

	context ={

		"products" : Product.objects.get(id = id)
		

	}

	return render(request, 'semiAppTemplates/edit.html', context)
	
def creates(request): #Create New Product 

	Product.objects.create(product_name = request.POST['name'], product_description = request.POST['description'], product_price= request.POST['price'])


	return redirect('/')
	
def updates(request, id):

	return render(request, 'semiAppTemplates/update.html')
	
def destroys(request,id):



	
	# destroyer = request.POST['remove']

	Product.objects.get(id=id).delete()




	
	return redirect('/')

