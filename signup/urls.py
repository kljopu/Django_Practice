from django.urls import path
from . import views


urlpatterns = [
    path("", views.signup, name = 'signup'),
    path("sign_in/", views.signIn, name = "sign_in"),

]