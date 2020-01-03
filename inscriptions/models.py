from django.db import models


#if this file is changed, run : python manage.py makemigrations inscriptions
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    punchline = models.TextField()
    type_text = models.CharField(max_length=20)
    imageUrl = models.URLField()


class GameMaster(models.Model):
    name = models.CharField(max_length=200)
    first = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    mail = models.EmailField()
    moreInfo = models.TextField()
    author = models.BooleanField()


class Event(models.Model):
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()


class Scenario(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    BEGINNER = 'Beginner'
    AVERAGE = 'Average'
    VETERAN = 'Veteran'
    LEVEL_OF_GAMES = ((BEGINNER,'Beginner'),(AVERAGE,'Average'),(VETERAN,'Veteran'),)
    level = models.CharField(max_length=10,choices=LEVEL_OF_GAMES, default=BEGINNER,)
    maximumPlayers = models.IntegerField()
    minimumPlayers = models.IntegerField()
    description = models.CharField(max_length=200)
    master = models.ForeignKey(GameMaster, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
