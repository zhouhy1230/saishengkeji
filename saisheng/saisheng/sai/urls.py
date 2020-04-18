from django.urls import path, re_path

from sai import views

urlpatterns = [
    path('put', views.PutView.as_view()),
    path('search', views.SearchView.as_view())
]
