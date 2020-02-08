from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def expense(request):
    "this is for test"
    return HttpResponse("This is my test process")
