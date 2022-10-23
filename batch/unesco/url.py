from django.urls import path

from . import views

app_name = 'unesco'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sites', views.ListView.as_view(), name='sites'),
    path('sites/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
