from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('remove_course/<int:id>', views.destroy),
    path('confirm_remove/<int:id>', views.remove)	   
]
