from django.shortcuts import render,redirect
from .models import Email
from django.contrib import messages

# Create your views here.

def index(request):


	return render(request, 'emailValidationAppTemplates/index.html')

def process(request):

	if Email.EmailManager.validEmail(request.POST['email']):
		Email.EmailManager.create(email = request.POST['email'])
		return redirect('/success')
	else:
		messages.error(request, 'This is an invalid email.')

		return redirect('/')


def success(request):

	context = {

		"emails" : Email.EmailManager.all()[::-1]
		# "names" : Email.e,
	}


	return render(request, 'emailValidationAppTemplates/success.html', context)

	