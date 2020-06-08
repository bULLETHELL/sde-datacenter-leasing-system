from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("lease/", views.lease, name="lease"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("reserve/", views.reserve, name="reserve"),
    path("lease_request/", views.lease_request, name="lease_request"),
    path("profile/<str:username>/settings/", views.profile_settings, name="profile_settings"),
    path("profile/<str:username>/loans/", views.loans, name="loans"),
]