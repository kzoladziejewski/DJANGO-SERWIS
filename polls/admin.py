# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name_of_quiz, Name_of_Question, Answer,User, Who_Answer
# Register your models here.

admin.site.register(Name_of_quiz)
admin.site.register(Name_of_Question)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(Who_Answer)