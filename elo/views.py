from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'elo/home.html' )
def mlb(request):
    return render(request, 'elo/mlb.html', {'title': 'MLB'} )
