from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import *

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    help_dict = {"help_page": "Welcome to the Help Page"}
    return render(request, "help.html", context = help_dict)

def blog(request):
    users = User.objects.all().order_by("first_name")
    user_dict = {"user_blog": users}
    return render(request, "blog.html", context = user_dict)
