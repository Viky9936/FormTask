# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User

class Useradmin(admin.ModelAdmin):
	list_display=('name','emailid','message','created_on')

	search_fields = ['name','emailid']


admin.site.register(User,Useradmin)