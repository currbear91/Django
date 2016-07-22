from django.shortcuts import render, redirect
import random
import string
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	return render(request, 'randomwordapp/index.html')

def formProcess(request):
	print request.session

	if "counter" in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1

	randomnum = random.randint(1, 14)
	request.session['randomstring'] = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for pos in range( 0,randomnum))
	
	return redirect(reverse('my_word_index'))

def deleteCount(request):
	if "counter" in request.session:
		del request.session['counter']


	return redirect (reverse('my_word_index'))




