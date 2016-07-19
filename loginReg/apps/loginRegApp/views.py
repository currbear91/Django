from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages



# Create your views here.
def index(request):

	return render(request, "loginRegAppTemplates/index.html")

# Create your views here.

def process(request):
	
	if User.userManager.validRegister(request.POST, request):
		error = True
		return redirect('/')
	else:
		error = False
		return redirect('/')


def success(request):

	if User.userManager.login(request.POST, request):
		context = {

			"user" : User.objects.get(email = request.POST['email'])
			# "names" : Email.e,
		}
	
		error = True

		return render(request, 'loginRegAppTemplates/success.html', context)

	else:
		error = False
		return redirect('/')


	