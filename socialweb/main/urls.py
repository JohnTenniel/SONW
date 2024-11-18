from django.urls import path, include
from . import views
from .views import Register

urlpatterns = [
    path('', views.main, name='main'),


    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),

]
