from django.db import models
from django.contrib import messages

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = 'Please enter course name greater than 3 characters'
        if len(postData['desc']) < 16:
            errors['desc'] = 'Please enter course description'
        return errors



class Course(models.Model):
    name = models.CharField(max_length= 255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    objects = CourseManager()

def display_courses():
    return Course.objects.all()

# def add_courses(request):
#     if request.method == 'POST':
#             errors = Course.objects.basic_validator(request.POST)
#             if len(errors) > 0:
#                 for key, value in errors.items():
#                      messages.error(request, value)
#     else:
#         Course.objects.create(name = request.POST['course_name'], desc = request.POST['course_desc'])
#         messages.success(request, 'Course added successfully')


# Create your models here.
