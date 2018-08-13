# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import Course
from ..login_registration.models import User

def index(request):
    courses = Course.objects.all()
    context = {
        "all_courses" : courses
    }
    return render(request, "courses_app/index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/courses') 
    else:
        new_course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'], created_by=User.objects.get(id=request.session['user_id']))
        print(new_course.name)
        print(new_course.desc)
        print(new_course.created_by)
        return redirect('/courses')


def delete(request, id):
    print('entered delete')
    my_user_id = User.objects.get(id=request.session['user_id']).id
    if(my_user_id == Course.objects.get(id=id).created_by.id):
        print('you can delete')
        b = Course.objects.get(id=id)
        b.delete()
    else:
        print('you cannot delete')
    # context = {
    #     "my_id" : my_course.id,
    #     "my_name" : my_course.name,
    #     "my_desc" : my_course.desc
    # }
    return redirect('/courses')

def edit(request, id):
    print('entered edit')       
    my_user_id = User.objects.get(id=request.session['user_id']).id
    if(my_user_id == Course.objects.get(id=id).created_by.id):
        print('you can edit')
        print('id')
        print(id)
        context={
            'course_id': id
        }
        return render(request, "courses_app/edit.html", context)
    else:
        print('you cannot edit')
        return redirect('/courses')

# def confirm_delete(request, id):
#     print("entered confirm_delete")
#     b = Course.objects.get(id=id)
#     b.delete()
#     return redirect('/')
def update(request, id):
    print('entered update')
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/courses/edit/' + id)
    else:
        b = Course.objects.get(id=id)
        b.name = request.POST['name']
        b.desc = request.POST['desc']
        b.save()
        print(b.name)
        print(b.desc)
    
    return redirect('/courses')


def join(request, id):
    print('entered join')
    my_user = User.objects.get(id=request.session['user_id'])
    my_course = Course.objects.get(id=id)
    my_course.students.add(my_user)
    return redirect('/courses')

def show(request, id):
    print('entered show')
    my_course_name = Course.objects.get(id=id).name
    my_course_students = Course.objects.get(id=id).students.all()
    print(my_course_students)
    print(my_course_name)
    context = {
        "my_course_name": my_course_name,
        "my_course_students": my_course_students
    }
    return render(request,"courses_app/show.html", context)

def clear(request):
    print('entered clear')
    courses = Course.objects.all()
    courses.delete()
    return redirect('/courses')


