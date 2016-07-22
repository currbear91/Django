from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):

	return render(request, 'userDashTemplates/index.html')
