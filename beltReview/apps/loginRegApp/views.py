from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse



# Create your views here.
def index(request):

	return render(request, "loginRegAppTemplates/index.html")

# Create your views here.

def process(request):

	
	if User.userManager.validRegister(request.POST, request):
		passflag = True
		return redirect(reverse('my_login_index'))
	
	else:
		passflag = False
		return redirect(reverse('my_login_index'))


def success(request):

	
	if User.userManager.login(request.POST, request):

		passflag = True

		return redirect(reverse('my_login_display'))

	else:
		passflag = False
		return redirect(reverse('my_login_index'))

def display(request):



	context = {
	
	'gal' : User.userManager.get(id = request.session['id'])
		
	}

	return render(request, 'loginRegAppTemplates/success.html', context)




def add(request):


	

	return render(request, 'loginRegAppTemplates/addbook.html')


















