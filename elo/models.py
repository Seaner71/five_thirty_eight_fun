from django.db import models

# Create your models here.

class Team(models.Model):
    abbreviation = models.CharField(max_length=4)
    city = models.CharField(max_length=70)
    nickname = models.CharField(max_length=70)
    colors = models.CharField(max_length=10)
    ## Add the foreign key from the ratings model
    #elo_rating = models.ForeignKey(Rating)
    def __str__(self):
        return self.abbreviation
