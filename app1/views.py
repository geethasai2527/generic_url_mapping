from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_string(request):
    return HttpResponse('this is first string')
def second_string(request):
    return HttpResponse('this is my second string')