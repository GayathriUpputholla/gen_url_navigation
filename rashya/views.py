from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sachin(request):
    return render(request,'sachin.html')
def seetha(request):
    return HttpResponse('<h1>THIS IS SEETHA httpresponse</h1>')    
