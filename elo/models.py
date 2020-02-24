from django.db import models

# Create your models here.

class Team(models.Model):
    abbreviation = models.CharField(max_length=4)
    city = models.CharField(max_length=70)
    nickname = models.CharField(max_length=70)
    colors = models.CharField(max_length=10)
    league = models.CharField(max_length=5, null=True)
    conference = models.CharField(max_length=30, null=True)
    division = models.CharField(max_length=30, null=True)
    ## Add the foreign key from the ratings model not needed
    # elo_rating = models.ForeignKey('EloRating', on_delete=models.CASCADE)
    def __str__(self):
        return self.abbreviation

class EloRating(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default = None)
    rating = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return str(self.rating)
