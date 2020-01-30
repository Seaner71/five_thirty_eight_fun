from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> ELO home</h1>')
def mlb(request):
    return HttpResponse('<h3> MLB ELO</h3>')
