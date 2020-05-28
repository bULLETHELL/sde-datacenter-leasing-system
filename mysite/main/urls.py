from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("lease/", views.lease, name="lease"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login")
]