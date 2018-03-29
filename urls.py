from django.urls import path
from first_app import views

urlpatterns = [
        path('welcome/',views.welcome),
        path('hello/',views.hello),
        path('img/',views.img)
        ]

