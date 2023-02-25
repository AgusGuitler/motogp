from django.db import models

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField(max_length=30)
    riders = models.CharField(max_length=50, blank=True, null=True)
    bike = models.CharField(max_length=30)
    constructor_titles = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    history = models.TextField()
    old_riders = models.TextField(max_length=500)

    def __str__(self):
        return self.team

class Rider(models.Model):
    id = models.AutoField(primary_key=True)
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
        return self.rider