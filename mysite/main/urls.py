from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile", views.profile, name="profile"),
    path("lease", views.lease, name="lease")
]