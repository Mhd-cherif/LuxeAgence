from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_residences, name = "home"),
    path('add/', views.add_residence, name = "add"),
    path('delete/<int:id>/', views.delete_data, name = "deletedata"),
    path('update/<int:id>/', views.update_data, name = "updatedata"),
]