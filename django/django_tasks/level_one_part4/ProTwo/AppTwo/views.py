from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    help_dict = {"help_page": "Welcome to the Help Page"}
    return render(request, "help.html", context = help_dict)

def blog(request):
    return render(request, "blog.html")
