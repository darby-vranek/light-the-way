from django.shortcuts import render, redirect, reverse
from django.contrib import sessions

from .models import *

# Create your views here.
def index(request, methods=['GET']):
	context = {
		'tags': Tag.objects.all(),
		'resources': Resource.objects.all()
	}
	return render(request, 'main_app/index.html', context=context)

def select(request, tag_id='', active_search='', methods=['GET']):

	if len(active_search) > 0:
		active_ids = active_search.split('_')

		if tag_id in active_ids:
			active_ids.remove(tag_id)
		else:
			active_ids.append(tag_id)

		url_to_show = '_'.join(active_ids)

	else:
		active_ids = []
		url_to_show = tag_id

	return redirect('/show/'+url_to_show)


def show_all(request):
	context = {
		'active_search':'',
		'tags':Tag.objects.all(),
		'resources':Resource.objects.all()
	}
	return render(request, 'main_app/search.html', context=context)


def show(request, tag_ids=''):
	search_tags = tag_ids.split('_')
	resources = list()
	for resource in Resource.objects.all():
		tags = resource.tags.filter(id__in=[int(tag) for tag in search_tags])
		if len(tags) > 0:
			resources.append(resource)
	context = {
		'active_search': tag_ids,
		'tags': Tag.objects.all(),
		'resources': resources
	}
	return render(request, 'main_app/search.html', context=context)
