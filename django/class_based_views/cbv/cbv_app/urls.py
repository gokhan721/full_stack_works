from django.urls import path, re_path
from cbv_app import views

app_name = "cbv_app"

urlpatterns = [
    path('',views.SchoolListView.as_view(), name = "list"),
    path('<pk>/', views.SchoolDetailView.as_view(), name="detail"),
    path('<pk>/update', views.SchoolUpdateView.as_view(), name="update"),
    path('create/', views.SchoolCreateView.as_view(), name="create"),
    path('<pk>/delete', views.SchoolDeleteView.as_view(), name="delete"),
]
