from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request , "index.html")

def contact(request):

    return render(request , "contact.html")

def about(request):

    return render(request , "about.html")

def learning(request):

    return render(request, "learning.html")


def sucesspage(request):

    return HttpResponse("<h1>this is sucess page</h1>")
