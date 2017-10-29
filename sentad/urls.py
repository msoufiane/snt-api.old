from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/auth/', include('authentication.urls')),
]
