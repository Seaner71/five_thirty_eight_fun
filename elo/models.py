from django.db import models

# Create your models here.

class Team(models.Model):
    abbreviation = models.CharField(max_length=4)
    city = models.CharField(max_length=70)
    nickname = models.CharField(max_length=70)
    colors = models.CharField(max_length=10)
    league = models.CharField(max_length=5)
    conference = models.CharField(max_length=30)
    division = models.CharField(max_length=30)
    ## Add the foreign key from the ratings model
    #elo_rating = models.ForeignKey(EloRating)
    def __str__(self):
        return self.abbreviation
''' Figure out connecting the Team and EloRating field
class EloRating(models.Model):
    abbreviation = models.ForeignKey(Team)
    rating = models.IntegerField()
'''
