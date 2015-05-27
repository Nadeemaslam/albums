from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from photos.forms import PictureForm
from django.core.context_processors import csrf

''' View to add Photos '''
def add_photos_view(request):
	if request.POST:
		form = PictureForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
	    form = PictureForm()
	return render(request,'addPhoto.html')