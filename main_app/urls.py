from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('create/', views.create, name='create'),
  path('delete/<int:item_id>/', views.delete, name="delete"),
]