from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third_string(request):
    return HttpResponse('this is my third string')
def fourth_string(request):
    return HttpResponse('this is my fourth string')