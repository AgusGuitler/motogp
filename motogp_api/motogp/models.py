from django.db import models

class Team(models.Model):
    team = models.CharField(max_length=30)
    riders = models.CharField(max_length=50, blank=True, null=True)
    bike = models.CharField(max_length=30)
    constructor_titles = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    history = models.TextField(max_length=300)
    old_riders = models.TextField(max_length=500)

    def __str__(self):
        return self.team, self.riders, self.bike, self.constructor_titles, self.sponsor, self.history, self.old_riders

class Rider(models.Model):
    rider = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    motogp_titles = models.IntegerField()
    moto2_titles = models.IntegerField()
    moto3_titles = models.IntegerField()
    moto3_debut = models.DateField()
    moto2_debut = models.DateField()
    motogp_debut = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    old_teams = models.ManyToManyField(Team, related_name="old_team")
    about_rider = models.TextField(max_length=500)

    def __str__(self):
        return self.rider, self.age, self.motogp_titles, self.moto2_titles, self.moto3_titles, self.moto3_debut, self.moto2_debut, self.motogp_debut, self.team, self.old_teams, self.about_rider