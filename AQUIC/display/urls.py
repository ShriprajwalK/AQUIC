from django.urls import path
from . import views

urlpatterns = [
    path('', views.value_list, name='value_list'),
    path('post/',views.post, name='post')
]
