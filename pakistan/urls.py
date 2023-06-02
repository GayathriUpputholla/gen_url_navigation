from django.urls import path
from pakistan.views import*
app_name='pakistan'
urlpatterns=[
    path('virat/',virat,name='virat'),
]