from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader


def index(request):
	template = loader.get_template('PersonalWebApp/index.html')
	return HttpResponse(template.render({}, request))
	# return redirect("https://www.linkedin.com/in/victorcalabuig/")
