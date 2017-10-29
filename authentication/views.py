from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from authentication.serializers import ProfileSerializer
from rest_framework.filters import OrderingFilter
from knox.views import LoginView as KnoxLoginView
from rest_framework.viewsets import ModelViewSet
from authentication.models import Account

from django.contrib.auth.signals import user_logged_in
from knox.models import AuthToken
from rest_framework.response import Response
from knox.settings import knox_settings
from django.contrib.auth import authenticate, login
from rest_framework import permissions, status


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = PageNumberPagination
    filter_backends = DjangoFilterBackend, OrderingFilter,
    filter_fields = ''


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        UserSerializer = knox_settings.USER_SERIALIZER
        account = authenticate(username=request.data.get('username', None), password=request.data.get('password', None))

        if account is not None:
            if account.is_active:
                login(request, account)
                token = AuthToken.objects.create(account)
                user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
                return Response({
                    'user': UserSerializer(account).data,
                    'token': token,
                })
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Invalid username and/or password.'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
