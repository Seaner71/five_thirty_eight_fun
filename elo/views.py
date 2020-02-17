from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.

def home(request):
    return render(request, 'elo/home.html' )
def mlb(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'elo/mlb.html', context )
