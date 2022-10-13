from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Studentapi/', views.StudentAPI.as_view()),#path('Studentapi/', views.Student_api),
    path('Studentapi/<int:pk>', views.StudentAPI.as_view()),#path('Studentapi/<int:pk>', views.Student_api),
]