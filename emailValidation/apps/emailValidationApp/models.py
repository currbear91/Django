from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):

	# def login(self, email, password):

	def validEmail(self, email):

		if not EMAIL_REGEX.match(email):
			return False
			print "Did not match"
		else:
			return True
			print "Match"

	# def register(self, **kwargs):


class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField()
	password = models.CharField(max_length = 255)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)
	userManager = UserManager()
