# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) < 5:
            errors.append("name must be morethan 5 characters")
        if len(postData['desc']) < 15:
            errors.append("desc should be more than 15 characters")
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="course_creator")
    students = models.ManyToManyField(User, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()