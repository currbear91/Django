from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(model.Model):

	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length = 45)
	password = models.CharField(max_length = 100)
	email = models.EmailField
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comment(model.Model):
	comment = models.TextField()
	user = models.ForeignKey(User)
	message_id = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Message(model.Model):
	message = models.TextField()
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

