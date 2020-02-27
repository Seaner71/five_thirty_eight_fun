from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.

def home(request):
    return render(request, 'elo/home.html' )
def mlb(request):
    teams = Team.objects.all()
    unique_conferences = Team.objects.values_list('conference', flat=True).distinct()
    unique_divisions = Team.objects.values_list('division', flat=True).distinct()
    context = {
        'teams': teams,
        'conferences':unique_conferences,
        'divisions' :unique_divisions

    }
    return render(request, 'elo/mlb.html', context )
