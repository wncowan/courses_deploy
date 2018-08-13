# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        "all_users" : users
    }
    return render(request, "login_registration/index.html", context)

def create(request):
    print('entered create')
    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1, confirm_password=request.POST['confirm_password'])
        request.session['user_id'] = new_user.id
        print('currently logged in: ')
        print(request.session['user_id'])
        request.session['action'] = "registered"
        print(request.session['user_id'])
        return redirect('/courses')

def login(request):
    print('entered login')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.filter(email=request.POST['email'])[0].id
        request.session['action'] = "logged in"
        print('currently logged in: ')
        print(request.session['user_id'])
        return redirect('/courses')

    return redirect('/')

def delete(request):
    print('entered delete')
    b = User.objects.all()
    b.delete()
    return redirect('/')    

def courses(request):
    print('entered success')
    return render(request, 'login_registration/courses.html')
