from __future__ import unicode_literals

from django.db import models
from decimal import Decimal, DecimalException
from django import forms


# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length = 255)
	product_description = models.TextField(max_length = 1000)
	product_price = models.DecimalField(max_digits = 10, decimal_places = 2)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
