from django.shortcuts import render
from django.conf import settings
from .models import Rider, Marc, Valen


# Create your views here.
"""def rider(request):
    
    title = "More about our riders"
    name = Rider.name
    age = Rider.age
    motogp_titles = Rider.motogp_titles
    moto2_titles = Rider.moto2_titles
    moto3_titles = Rider.moto3_titles
    moto3_debut = Rider.moto3_debut
    moto2_debut = Rider.moto2_debut
    motogp_debut = Rider.motogp_debut
    current_team = Rider.current_team
    old_teams = Rider.old_teams
    about_rider = Rider.about_rider

    context = {
        "name": name,
        "age": age,
        "motogp_titles": motogp_titles,
        "moto2_titles": moto2_titles,
        "moto3_titles": moto3_titles,
        "moto3_debut": moto3_debut,
        "moto2_debut": moto2_debut,
        "motoGp_debut": motogp_debut,
        "current_team": current_team,
        "old_teams": old_teams,
        "about_rider": about_rider,
    }

    return render(request, "rider.html", context)"""

# Vista para Marc

def marc(request):

    title = "More about our riders"
    name = Marc.name
    age = Marc.age
    motogp_titles = Marc.motogp_titles
    moto2_titles = Marc.moto2_titles
    moto3_titles = Marc.moto3_titles
    moto3_debut = Marc.moto3_debut
    moto2_debut = Marc.moto2_debut
    motogp_debut = Marc.motogp_debut
    current_team = Marc.current_team
    old_teams = Marc.old_teams
    about_rider = Marc.about_rider

    context = {
        "name": name,
        "age": age,
        "motogp_titles": motogp_titles,
        "moto2_titles": moto2_titles,
        "moto3_titles": moto3_titles,
        "moto3_debut": moto3_debut,
        "moto2_debut": moto2_debut,
        "motoGp_debut": motogp_debut,
        "current_team": current_team,
        "old_teams": old_teams,
        "about_rider": about_rider,
    }

    return render(request, "rider.html", context)

def valen(request):

    title = "More about our riders"
    name = Valen.name
    age = Valen.age
    motogp_titles = Valen.motogp_titles
    moto2_titles = Valen.moto2_titles
    moto3_titles = Valen.moto3_titles
    moto3_debut = Valen.moto3_debut
    moto2_debut = Valen.moto2_debut
    motogp_debut = Valen.motogp_debut
    current_team = Valen.current_team
    old_teams = Valen.old_teams
    about_rider = Valen.about_rider

    context = {
        "name": name,
        "age": age,
        "motogp_titles": motogp_titles,
        "moto2_titles": moto2_titles,
        "moto3_titles": moto3_titles,
        "moto3_debut": moto3_debut,
        "moto2_debut": moto2_debut,
        "motoGp_debut": motogp_debut,
        "current_team": current_team,
        "old_teams": old_teams,
        "about_rider": about_rider,
    }

    return render(request, "rider.html", context)