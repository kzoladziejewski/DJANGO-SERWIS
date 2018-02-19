# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import  python_2_unicode_compatible
# Create your models here.

class Question(models.Model):
    question_text = models.DateTimeField("Data publikacji")
    #question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'Memo={0}, Tag={1}'.format(self.question_text, self.question_text)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    number_question = models.CharField(max_length=200, default="Pytanie nr:")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Date(models.Model):
    data_pytania = models.DateTimeField("Date of publish")

    def __str__(self):
        return self.data_pytania