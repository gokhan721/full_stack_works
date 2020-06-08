from django.shortcuts import render
from auth_app.forms import *


# Django built-in func for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'auth_app/index.html')


@login_required
def special(request):
    return HttpResponse("You are awesomeee by passing login_required!!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # commit=False not to get error
            profile = user_profile_form.save(commit=False)
            profile.user = user  # OneToOne Relationship

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.error, user_profile_form.errors)

    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()

    return render(request,
                  "auth_app/registration.html",
                  context={"user_form": user_form,
                           "user_profile_form": user_profile_form,
                           "registered": registered})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Someone try to login and failed!")
            print(f"Username: {username} and Password: {password}")
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, "auth_app/login.html")
