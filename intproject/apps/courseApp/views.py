from django.shortcuts import render, redirect
from .models import Course
from ..loginRegApp.models import User 
from django.db.models import Count
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):

	context = {

		"courses" : Course.objects.all()
	}

	return render(request, 'courseAppTemplates/index.html', context)

def process(request):

	Course.objects.create(course_name = request.POST['name'], course_description = request.POST['description'])


	return redirect(reverse('my_course_index'))

def delete(request, id):

	

	context = {

		"courses" : Course.objects.get(id=id)
	}

	return render(request, 'courseAppTemplates/delete.html', context)

def destroy(request, id):

	blah = Course.objects.get(id=id)

	if request.POST[u'delete']  == "Yes, I would LOVE to delete this":
		blah.delete()
		return redirect(reverse('my_course_index'))

	else:
		return redirect(reverse('my_course_index'))

def usercourse(request):

	if request.method == 'POST':
		print "*" * 50
		print request.POST
		our_user = User.objects.get(id = request.POST['user'])
		print "*" * 50
		our_course = Course.objects.get(id = request.POST['course'])
		our_course.user_id.add(our_user)
		our_course.save()

 	c = Course.objects.annotate(num_users = Count('user_id'))
	context = {

		"users" : User.objects.all(),
		"courses": Course.objects.all(),
		"count" : c,	
		"temp": Course.objects.all()
	}	


	return render(request , "courseAppTemplates/usercourses.html", context)


