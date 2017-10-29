from knox.views import LogoutView, LogoutAllView
from authentication.views import LoginView
from django.conf.urls import url

urlpatterns = [
    url(r'login/', LoginView.as_view(), name="login_view"),
    url(r'logout/', LogoutView.as_view(), name="logout_view"),
    url(r'logoutall/', LogoutAllView.as_view(), name="logout_all_view"),
]
