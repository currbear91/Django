from __future__ import unicode_literals
from ..loginRegApp.models import User
from django.db import models
from django.contrib import messages


# Create your models here.

class ReviewManager(models.Manager):


	def isValid(self, reviewInfo, request):

		passflag = True

		if len(reviewInfo['bookreview']) < 1:
			messages.error(request, "Review must be 45 characters long.")
			passflag = False

		if len(reviewInfo['book_title']) <= 1:
			messages.error(request, "Please put in a valid book title.")
			passflag = False		

		if len(reviewInfo['addauthor']) < 1:
			messages.error(request, "Please put in a valid author name.")
			passflag = False

		return passflag	

	def createReview(self, reviewInfo, request):

		print reviewInfo['addauthor']

		if len(Author.objects.filter(author = reviewInfo['addauthor'])) == 0:  #If author doesnt exist,
			Author.objects.create(author = reviewInfo['addauthor'])		#Create this author typed in

		if len(Book.objects.filter(title = reviewInfo['book_title'])) == 0:  #If title of book doesnt exist,
			Book.objects.create(title = reviewInfo['book_title'], author = Author.objects.get(author = reviewInfo['addauthor']))

		else:
			Book.objects.get(title = reviewInfo['book_title']) 		#Find books that exist by author typed in the book title text box

		Review.objects.create(review=reviewInfo['bookreview'], ratings= reviewInfo['rating'], user=User.objects.get(id = request.session['id']), book = Book.objects.get(title=reviewInfo['book_title']))

		# Check database if book title/author already exists, if not create a new book/author
			# Make review



class Author(models.Model):
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)



class Book(models.Model):
	title = models.CharField(max_length=255)
	author =  models.ForeignKey(Author)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	

class Review(models.Model):
	review = models.TextField(max_length=1000)
	ratings = models.CharField(max_length=5)
	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	ReviewManager= ReviewManager()
	objects = models.Manager()
















