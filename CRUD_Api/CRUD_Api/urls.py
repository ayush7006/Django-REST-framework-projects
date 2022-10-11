
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Studentapi/', views.Student_api),#funtion based
    #path('Studentapi/', views.StudentAPI.as_view()),#class based
]
