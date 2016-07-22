from django.shortcuts import render, HttpResponse
import datetime
from django.core.urlresolvers import reverse

def index(request):

	now = datetime.datetime.now()
	
	context = {
	"Date":now.strftime ("%b %d, %Y"),
	"Time": now.strftime ("%I:%M %p")
	
	}
	return render(request, 'timedisplay/page.html', context)
# Create your views here.
