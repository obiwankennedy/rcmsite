from django.contrib import admin

# Register your models here.
from .models import Game, Event, GameMaster, Scenario

admin.site.register(Game)
admin.site.register(Event)
admin.site.register(GameMaster)
admin.site.register(Scenario)
