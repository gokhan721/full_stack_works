from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *

# Create your views here.

def home(request):
    return HttpResponse("Hello Home")

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'AccessRecord': webpages_list}
    return render(request, "index.html", context = date_dict)
