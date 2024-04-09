from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

#index page include form to add a course, and a table of data with link to remove course 
def index(request):
    context = {
        'courses': models.display_courses()
    }
    return render(request, 'index.html', context)

#this function for checking if we have errors in post request "form"
#if we have any error it will added in dectionary called errors
#else: if we don't have any error create course
def add_course(request):
     if request.method == 'POST':
            errors = models.Course.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                     messages.error(request, value)
                return redirect('/')
            else:
                models.Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
                messages.success(request, 'Course added successfully')
     return redirect('/')
     
#this function will render remove page
def destroy(request, id):
     context = {
          'course': models.Course.objects.get(id = id)
     }
     return render(request, 'remove.html', context)

#this function will remove the course from db
def remove(request, id):
     course_id = id
     models.Course.objects.filter(id = course_id).delete()
     return redirect('/')
         


     

# Create your views here.
