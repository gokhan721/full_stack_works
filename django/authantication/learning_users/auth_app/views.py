from django.shortcuts import render
from auth_app.forms import *

# Create your views here.
def index(request):
    return render(request, 'auth_app/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False) # commit=False not to get error
            profile.user = user # OneToOne Relationship


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
                context = {"user_form": user_form,
                        "user_profile_form": user_profile_form,
                        "registered": registered})
