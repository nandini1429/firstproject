from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    msg = "<h1>Hello good evening, welcome to django framework</h1>"
    return HttpResponse(msg)
