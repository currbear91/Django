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
		error = True
		return redirect(reverse('my_login_index'))
	else:
		error = False
		return redirect(reverse('my_login_index'))


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
		return redirect(reverse('my_login_index'))


	