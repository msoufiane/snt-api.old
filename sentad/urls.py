from graphene_django.views import GraphQLView
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.conf.urls import url, include
from sentad.schema import schema
from django.conf import settings
import os

DJANGO_ENV = os.environ.get("DJANGO_ENV", "development")

if DJANGO_ENV == "development":
    urlpatterns = [
        url(r'^auth/', include('authentication.urls')),
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^', GraphQLView.as_view(graphiql=True, schema=schema)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns = [
        url(r'^auth/', include('authentication.urls')),
    ]
