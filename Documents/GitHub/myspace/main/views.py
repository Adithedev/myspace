from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main import *
# Create your views here.

def acct(request):
    return render(request, "contacts.html", {})

def projects(request):
	return render(request, "project.html", {})
    
def home(request):
	return render(request, "main.html", {})	