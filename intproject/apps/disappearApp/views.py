from django.shortcuts import render,redirect, HttpResponse

# Create your views here.

def index(request):

		return render(request,"disappearAppTemplates/index.html" )

def showNinjas(request):

	return render(request, 'disappearAppTemplates/all.html')


# def showNinja(request, color):

def show(request, color):
	if color == "red":
		context = {
			"color": ' ../static/disappearAppImg/ralph.png'
		}
	elif color == "orange":
		
		context = {"color": ' ../static/disappearAppImg/michelangelo.png'}
	
	elif color == "blue":

		context = {"color": '../static/disappearAppImg/Leonardo.gif'}
	
	elif color == "purple":
		
		context = {"color": '../static/disappearAppImg/donatello.gif'}
	
	else:

		context = {"color": '../static/disappearAppImg/MeganFox.png'}
	
	return render(request, 'disappearAppTemplates/show.html', context)

	# if(color == "red"):
	# 	return HttpResponse('<img src="../static/disappearAppImg/ralph.png"> ')
	# elif(color== "orange"):
	# 	return HttpResponse('<img src="../static/disappearAppImg/michelangelo.png"> ')
	# elif(color== "blue"):
	# 	return HttpResponse('<img src="../static/disappearAppImg/Leonardo.gif"> ')
	# elif(color== "purple"):
	# 	return HttpResponse('<img src="../static/disappearAppImg/Donatello.gif">')
	# else:
	# 	return HttpResponse('<img src="../static/disappearAppImg/MeganFox.png">')
	
	# print "|" * 50
	

	# return redirect('/showNinjas')

