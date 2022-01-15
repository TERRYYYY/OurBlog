from django.urls import path
from blog import views

urlpatterns = [
    path('', views.helloworld, name='helloworld'),
]
