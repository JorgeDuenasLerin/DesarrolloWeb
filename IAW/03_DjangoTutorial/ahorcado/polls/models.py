import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def escribete_en_consola(self):
        print("********* CONSOLA *********")
        print(self.question_text)
        print(self.pub_date)

    def ha_sido_publicada_hacepoco(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Youtuber(models.Model):
    nombre = models.CharField(max_length=200)
    pasta = models.IntegerField(default=0)
    comenzo_a_estafar_en = models.DateField(null=True)
    canal = models.URLField()

    def __str__(self):
        return self.nombre + ' - ' + str(self.pasta)
