from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse
# Create your views here.

def indexs(request):
	print "*" * 50
	# print Product.objects.product_name()
	print "*" * 50


	context ={

		"useres" : User.objects.all()
		

	}

	return render(request, 'semiAppTemplates/index.html', context)
	
def shows(request, id):

	context ={

		"products" : User.objects.get(id = id)
		

	}

	
	return render(request, 'semiAppTemplates/show.html', context)
	
def news(request): #Add New product for

	return render(request, 'semiAppTemplates/new.html')
	
def edits(request, id):

	context ={

		"products" : User.objects.get(id = id)
		

	}

	return render(request, 'semiAppTemplates/edit.html', context)
	
def creates(request): #Create New Product 

	User.objects.create(user_name= request.POST['name'], email= request.POST['email'], user_level = request.POST['level'])


	return redirect(reverse('my_semi_indexs'))
	
def updates(request, id):

	return render(request, 'semiAppTemplates/update.html')
	
def destroys(request,id):



	
	# destroyer = request.POST['remove']

	User.objects.get(id=id).delete()




	
	return redirect(reverse('my_semi_indexs'))

