from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'autos'
urlpatterns = [
    path('', views.AutosListView.as_view(), name='all'),
    path('create/', views.AutoCreate.as_view(), name='auto_create'),
    path('<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('makes/', views.MakesListView.as_view(), name='make_list'),
    path('makes/create/', views.MakeCreate.as_view(), name='make_create'),
    path('makes/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('makes/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]

# Note that make_ and auto_ give us uniqueness within this application
