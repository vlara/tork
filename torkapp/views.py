from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("OK!")

def csvupload(request):
	return HttpResponse("CSV UPLOAD!")
