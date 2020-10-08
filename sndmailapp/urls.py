from django.urls import path
from sndmailapp import views

urlpatterns = [
    path('',views.sendMailApp)
]
