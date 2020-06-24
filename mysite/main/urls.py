from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("lease/", views.lease, name="lease"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("reserve/", views.reserve, name="reserve"),
    path("reservation_request/", views.reserve_request, name="reservation_request"),
    path("lease_request/", views.lease_request, name="lease_request"),
    path("return/", views.returnLoan, name="returnLoan"),
    path("return_request/", views.return_request, name="return_request"),
    path("change_password/", views.change_password_request, name="change_password"),
]
