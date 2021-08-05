from django.db import models
from simple_history.models import HistoricalRecords

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()



from simple_history import register
from django.contrib.auth import get_user_model

register(get_user_model(), app="demo_django_versioning")
