from django.contrib import admin
from api import views
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router= DefaultRouter()
router.register('studentapi', views.StudentViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(),name='TokenObtainPair'),
    path('refreshtoken/', TokenRefreshView.as_view(),name='TokenRefresh'),
    path('verifytoken/', TokenVerifyView.as_view(),name='TokenVerify'),
   
]
