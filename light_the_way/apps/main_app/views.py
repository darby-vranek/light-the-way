from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	context = {
		'tags': Tag.objects.all(),
		'resources': Resource.objects.all()
	}
	return render(request, 'main_app/index.html', context=context)

def select(request, tag_id):
	context = {
		'tags': Tag.objects.all(),
		'resources': Resource.objects.filter(tags__id=tag_id)
	}
	return render(request, 'main_app/index.html', context=context)
