from django import views
from django.urls import path
from tasks import views


urlpatterns=[
    path('',views.Home,name='create_list'),
    path('Update/<str:pk>/',views.Update,name='Update'),
    path('Delete/<str:pk>/',views.Delete,name='Delete'),
]