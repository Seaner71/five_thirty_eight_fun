from django.db import models
from django import forms

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
'''
class QueryForm(forms.Form):
    choice_name = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['conference'].choices = Event.objects.all().values_list('conference').distinct()

'''
