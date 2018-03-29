from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse ("welcome to my world")

def hello(request):
    word = "am doing great"
    return render(request, 'first_app/hello.html/', {'ver':word})

def img(request):
    return render (request,'first_app/static_file.html/')