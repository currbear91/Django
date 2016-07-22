from __future__ import unicode_literals

from django.db import models
from ..loginRegApp.models import User

# Create your models here.

class Course(models.Model):
	course_name = models.CharField(max_length = 255)
	course_description = models.TextField(max_length = 1000)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now= True)
	user_id = models.ManyToManyField(User)
