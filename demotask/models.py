# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name = "Username")
    emailid = models.EmailField(unique=True)
    message = models.TextField()
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + " : " + self.emailid