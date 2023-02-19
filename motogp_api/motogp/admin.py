from django.contrib import admin

# Register your models here.
from .models import Team, Rider

admin.site.register(Team)
admin.site.register(Rider)