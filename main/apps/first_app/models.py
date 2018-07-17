from django.db import models
import re
from django.contrib import messages

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        #Checking for length
        if len(postData['course_name']) < 5:
            errors['course'] = "Course name must have at least 5 characters"
        if len(postData['course_description']) < 15:
            errors['description'] = "Course description must have at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()