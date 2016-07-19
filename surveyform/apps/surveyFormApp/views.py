from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	return render(request, 'surveyFormTemplates/index.html')

def formProcess(request):
	print request.session
	if "counter" in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1

	request.session['data'] = {

		'Name' :request.GET['name'],
		'Dojo Location': request.GET['dojolocation'],
		'Favorite Language': request.GET['favLang'],
		'Comments': request.GET['comments']

	}
	print request.GET
	print '#' * 50
	return redirect('/showResults')

def showResults(request):
	print request.session
	return render(request, 'surveyFormTemplates/results.html')
