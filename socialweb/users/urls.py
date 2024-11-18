from django.urls import path, include
from . import views
from .views import send_request, accept_request


urlpatterns = [

    path('add-friends/<int:id>', send_request, name='add-friends'),
    path('accept/<int:id>', accept_request, name='accept'),


]
