from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Review, ReviewManager, Author, Book



def specificReview(request):

	if Review.ReviewManager.createReview(request.POST, request):

		return render(request ('beltreviewtemplates/show.html'))



def bookReview(request):

	if Review.ReviewManager.isValid(request.POST, request):
		Review.ReviewManager.createReview(request.POST, request)
		print request.POST
		return redirect(reverse('my_specific_review'))
	else:
	
		redirect(reverse('my_book_review'))


