from django.shortcuts import render
from .models import Comment, Message 

# Create your views here.

def index(request):
  print(User.objects.all())
  # A list of objects (or an empty list)
  User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
  # Creates a user object
  print(User.objects.all())
  # A list of objects (or an empty list)
  u = User.objects.get(id=1)
  print(u.first_name)
  u.first_name = "Joey"
  u.save()
  j = User.objects.get(id=1)
  print(j.first_name)
  # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
  print(User.objects.get(first_name="mike"))
  # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO BE CHANGED ***
  users = User.objects.raw("SELECT * from my_app_name_user")
  # Uses raw SQL query to grab all users (equivalent to User.objects.all()), which we iterate through below
  for user in users:
    print user.first_name
  return HttpResponse("ok")