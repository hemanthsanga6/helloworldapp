from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.http import JsonResponse 

def index(request):
    data = {'Message' : 'Hello World!'}
    return JsonResponse(data)
