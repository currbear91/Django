from django.shortcuts import render, redirect
import datetime
import random
import string
# Create your views here.

def index(request):


	if "gold" in request.session:
		request.session["gold"] += 0
	else:
		request.session["gold"] = 0

	if 'messages' in request.session:
		pass
	else:
		request.session["messages"] = []
	return render(request, 'ninjaGoldTemplates/index.html')

def process(request):

	now = datetime.datetime.now()
	date_object = now.strftime('%Y/%m/%d %I:%M%p')
	random.randrange(0,2)
	# request.session['gold'] = 0

	if request.POST['building'] == 'farm':
		goldcoin = random.randrange(10,21)
		stringval = ''.join(["You have earned " , str(goldcoin) , " gold. " , str(date_object)])
		request.session['messages'].append(stringval)
		request.session['gold'] += goldcoin
		print goldcoin

	if request.POST['building'] == 'cave':
		goldcoin = random.randrange(5,11)
		stringval = ''.join(["You have earned " , str(goldcoin) , " gold. " , str(date_object)])
		request.session['messages'].append(stringval)
		request.session['gold'] += goldcoin
		print goldcoin

	if request.POST['building'] == 'house':
		goldcoin = random.randrange(2,6)
		stringval = ''.join(["You have earned " , str(goldcoin) , " gold. " , str(date_object)])
		request.session['messages'].append(stringval)
		request.session['gold'] += goldcoin
		print goldcoin

	if request.POST['building'] == 'casino':
		goldcoin = random.randrange(-50, 51)
		request.session['gold'] += goldcoin
		if goldcoin < 0:	
			stringval = ''.join(["You have lost " , str(goldcoin) , " gold. " , str(date_object)])
			request.session['messages'].append(stringval)
		else:
			stringval = ''.join(["You have earned " , str(goldcoin) , " gold. " , str(date_object)])
			request.session['messages'].append(stringval)

	return redirect('/')

def clear(request):

	if request.POST['clear'] =='Clear Gold History':
		del request.session['messages']
		del request.session['gold']

	return redirect('/')
	

	# print "*" * 50
	# print request.session
	# print "*" * 50


# 	# request.session['goldcnt'] = {

# 	# 	'Farm' :request.POST['farm'],
# 	# 	'Dojo Location': request.POST['dojolocation'],
# 	# 	'Favorite Language': request.POST['favLang'],
# 	# 	'Comments': request.POST['comments']
	
