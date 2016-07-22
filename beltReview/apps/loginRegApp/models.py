from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from django.contrib import messages


EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):

	# def login(self, email, password):

	def validRegister(self, userInfo,request):
		#userInfo is a dictionary of stuff from request.POST['']

		
		error = True

		password = userInfo['password']


		if len(userInfo['first_name']) < 1:
			messages.error(request, "First name cannot be empty!")
			error = False
		if len(userInfo['last_name']) < 1:
			messages.error(request,"Last Name cannot be empty!")
			error = False
		if len(userInfo['email']) < 1:
			messages.error(request, "Email cannot be empty")
			error = False
		if not EMAIL_REGEX.match(userInfo['email']):
			messages.error(request,"Invalid Email")
			return False
		if len(User.objects.filter(email = userInfo['email'])) > 0:
			messages.error(request, "This email already exists.")
			error = False
		if len(userInfo['password']) < 1:
			messages.error(request,"Password cannot be empty!" )
			error = False
		if len(userInfo['confirm']) < 1:
			messages.error(request,"Password cannot be empty!")
			error = False
		if userInfo['password'] != userInfo['confirm']:
			messages.error(request, "Passwords must match")
			error = False
		if error == True:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			User.objects.create(email = userInfo['email'], first_name = userInfo['first_name'], last_name = userInfo ['last_name'], password = hashed)
			messages.success(request, "Congratulations on making your new account!")
		return error

		# else:
		# 	print "Match"

	def login(self, userInfo, request):

		passflag = False
		print userInfo
		if len(User.objects.filter(email = userInfo['email'])) > 0:
			guy = User.objects.get(email = userInfo['email'])
			hashed = guy.password 
			hashed = hashed.encode('utf-8')
			password = userInfo['password']
			password = password.encode('utf-8')
			#User = Table, 
			# Objects is the table manages
			# Get is a method of the manager
			#.get returns user object and calling .password on that object
			if bcrypt.hashpw(password, hashed) == hashed:
				passflag = True
				request.session['id'] = guy.id 
		if not passflag:
			messages.warning(request, "The email you entered was not found.")
			

		return passflag


 
	


class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField()
	password = models.CharField(max_length = 255)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()

