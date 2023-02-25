from django.shortcuts import render
from django.conf import settings
from .models import Rider, Team


# Create your views here.
def rider(request):
    riders = Rider.objects.all()
    
    return render(request, "rider.html", {"riders": riders})

def team(request):
    teams = Team.objects.all()
    
    return render(request, "team.html", {"teams":teams})
