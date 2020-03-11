from django.urls import path
from pagination import views

urlpatterns = [
        path('', views.FormListView.as_view(), name='listview'),
        path('form', views.form_view, name = 'form'),
        path('about', views.about_view, name='about')
        ]
