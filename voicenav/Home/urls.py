
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('home', index, name="index"),
    path('vr', voice, name='voice'),
]