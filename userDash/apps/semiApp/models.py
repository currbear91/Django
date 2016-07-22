from __future__ import unicode_literals

from django.db import models
from decimal import Decimal, DecimalException
from django import forms


# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	level = models.CharField(max_length = 9)
