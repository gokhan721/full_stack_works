from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from cbv_app import models
from django.urls import reverse_lazy


# from django.http import HttpResponse
#
# class CBVView(View):
#     template_name = "index.html"
#
#     def get(self, request):
#         return HttpResponse("CBV cools!!!")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'  # default school_list
    model = models.School
    template_name = "cbv_app/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = "cbv_app/school_detail.html"


class SchoolCreateView(CreateView):
    model = models.School
    fields = ("name", "principal", "location")


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ["name", "principal"]


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("cbv_app:list")
