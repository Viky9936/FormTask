# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from .models import User
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def userView(request):
    if request.method=='POST':

        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            print("is valid--------")
            user = form.save(commit=False)
            print(user, user.name)
            user.save()
            return HttpResponseRedirect(reverse('base'))#redirect('base', pk=user.id))
        else:
            print(form.errors)
            messages.error(request, "Error")
            print("----", messages)    

        print("not ------------")

        # return render(request, 'demotask/base.html', {'form':form})

    else:
        form = UserForm() 

    return render(request, 'demotask/base.html', {'form':form})


"""def user_new(request):
    form = UserForm()
    return render(request, 'demotask/showdata.html',{'form':form})"""