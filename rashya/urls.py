from django.urls import path
from rashya.views import*
app_name='rashya'
urlpatterns=[
    path('sachin/',sachin,name='sachin'),
]