# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

from django.utils.encoding import  python_2_unicode_compatible
# Create your models here.

class Name_of_quiz(models.Model):
    Name = models.CharField(max_length=20)
    Grand = models.CharField(max_length=200)
    Date_of_public = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Name


class Name_of_Question(models.Model):
    Date_of_Add = models.DateTimeField(default=timezone.now)
    Membership_of_Question = models.ForeignKey(Name_of_quiz, on_delete=models.CASCADE)
    Text_of_Question = models.CharField(max_length=255, default=None, blank=True)
    Image_of_Question = models.ImageField(default=None, blank=True)
    Correct_Answer = models.CharField(max_length=255)
    def __str__(self):
        return self.Text_of_Question

class User(models.Model):
    ip = models.CharField(max_length=25, default="RADOM")
    def __str__(self):
        return self.ip

class Answer(models.Model):
    Text_of_Answer = models.CharField(max_length=255)
    Answer_To_Question = models.ForeignKey(Name_of_Question, on_delete=models.CASCADE, default=None)
    Number_Of_Answer = models.IntegerField(default=0)
    def __str__(self):
        return self.Text_of_Answer

class Who_Answer(models.Model):
    Who_Answer = models.ManyToManyField(User, default="None")
    Where_Answer = models.ManyToManyField(Name_of_Question,related_name=None, default=None)
    Who_Answer = models.ForeignKey(User, on_delete=models.CASCADE)
    How_Many = models.IntegerField(default=0)
