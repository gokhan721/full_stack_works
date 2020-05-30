from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.meta_forms import NewUserForm
# from AppTwo.models import * => list users with fake pop

# Create your views here.
def index(request):
    return render(request, "base.html")

def help(request):
    help_dict = {"help_page": "Welcome to the Help Page"}
    return render(request, "help.html", context = help_dict)
'''
=> list users with fake pop

def blog(request):
    users = User.objects.all().order_by("first_name")
    user_dict = {"user_blog": users}
    return render(request, "blog.html", context = user_dict)
'''

def blog(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Erro form invalid")

    return render(request, "blog.html", context = {"form": form})
