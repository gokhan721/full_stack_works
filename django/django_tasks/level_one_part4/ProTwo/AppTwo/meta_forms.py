from django import forms
from AppTwo.models import *


class NewUserForm(forms.ModelForm):
    # form fields can be şnştşated to use validation
    class Meta:
        model = User
        fields = "__all__"
