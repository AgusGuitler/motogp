from django.db import models

class Team(models.Model):
    team = models.CharField(max_length=30)
    rider_one = models.CharField(max_length=50)
    rider_two = models.CharField(max_length=50)
    bike = models.CharField(max_length=30)
    constructor_titles = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    history = models.CharField(max_length=300)

    def __str__(self):
        return self.team, self.rider_one, self.rider_two, self.bike, self.constructor_titles, self.sponsor, self.history

class Rider(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    motogp_titles = models.IntegerField()
    moto2_titles = models.IntegerField()
    moto3_titles = models.IntegerField()
    moto3_debut = models.DateField()
    moto2_debut = models.DateField()
    motogp_debut = models.DateField()
    team = models.CharField(max_length=50)
    #team = models.ForeignKey(Team, on_delete=models.CASCADE)
    old_teams = models.CharField(max_length=300)
    about_rider = models.CharField(max_length=500)

    def __str__(self):
        return self.name, self.name, self.age, self.motogp_titles, self.moto2_titles, self.moto3_titles, self.moto3_debut, self.moto2_debut, self.motogp_debut, self.team, self.old_teams, self.about_rider

class Marc(Rider):
    name = "Marc Márquez"
    age = 29
    motogp_titles = 8
    moto2_titles = 1
    moto3_titles = 1
    moto3_debut = 2008
    moto2_debut = 2010
    motogp_debut = 2013
    team = "Repsol Honda"
    old_teams = "Repsol Honda"
    about_rider = "Ha ganado ocho títulos del Campeonato del Mundo de Motociclismo en tres categorías diferentes: 125cc (2010), Moto2 (2012) y seis veces en MotoGP (2013, 2014, 2016, 2017, 2018 y 2019).3​ Desde 2013 es piloto del equipo Repsol Honda,4​ donde ha acumulado 50 victorias y 78 podios en 105 carreras disputadas. En febrero de 2020 extendió su contrato con Honda hasta 2024. En su primera temporada en la categoría, se hizo con el Campeonato del Mundo de Motociclismo, convirtiéndose en el piloto más joven en ganar un campeonato de la máxima categoría de este deporte (MotoGP), superando así el récord de Freddie Spencer. Es, además, el piloto más joven de la historia en ser bi, tri, tetra, penta y hexa campeón de la categoría reina del motociclismo."

class Valen(Rider):
    name = "Valentino Rossi"
    age = 43
    motogp_titles = 9
    moto2_titles = 1
    moto3_titles = 1
    moto3_debut = 1996
    moto2_debut = 1998
    motogp_debut = 2000
    team = "Retired"
    old_teams = "Repsol Honda, Yamaha, KTM, Ducati"
    about_rider = "Actualmente, es el piloto con más podios (235) en la historia del Mundial de Motociclismo, y además ha conseguido el mayor número de victorias (89), podios (199) y vueltas rápidas (76) en MotoGP. Es el único piloto en la historia del motociclismo que ha ganado el título en cuatro clases diferentes: 125cc (1), 250cc (1), 500cc (1) y MotoGP (6), además de ser el único piloto que ha ganado el título de la categoría reina en cuatro tipos diferentes de motocicletas, debido al cambio de reglamento en los años: Honda de 500 cc de 2 tiempos, Honda de 990 cc de 4 tiempos, Yamaha de 990 cc de 4 tiempos, Yamaha de 800 cc de 4 tiempos."

class Repsol_Honda(Team):
    team = "Repsol Honda"
    rider_one = "Marc Márquez"
    rider_two = "Joan Mir"
    bike = "RC213V"
    constructor_titles = 23
    sponsor = "Repsol, RedBull"
    history = "Honda surge, oficialmente, en el año 1946 en Hamamatsu, Japón, bajo el nombre de Honda Technical Research Institute (Instituto Honda de Investigaciones Técnicas). Un año después, se crea el primer producto de la marca."