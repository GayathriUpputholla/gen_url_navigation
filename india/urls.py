from django.urls import path
from india.views import*
app_name='india'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]