from django.urls import path

from . import views

urlpatterns = [
    path("singup/", views.SignUpViews.as_view(), name="sign_up"),
]
