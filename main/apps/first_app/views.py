from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request,'first_app/index.html',context)

def delete(request,number):
    context ={
        'course_to_be_edited':Course.objects.get(id=number)
    }
    print(context)
    return render(request,'first_app/delete.html',context)

def addcourse(request):
    errors = Course.objects.basic_validator(request.POST)

    if len(errors):
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['course_name'],description=request.POST['course_description'])
        return redirect('/')

def processdelete(request,number):
    course_to_be_deleted = Course.objects.get(id=number)
    course_to_be_deleted.delete()
    return redirect('/')