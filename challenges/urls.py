from django.urls import path
from . import views


#URLS que serão passadas no browser
urlpatterns = [
    path("", views.index, name="index"), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]