from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import authenticate, login

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from knox.views import LoginView as KnoxLoginView
from knox.settings import knox_settings
from knox.models import AuthToken


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    serializer_class = knox_settings.USER_SERIALIZER
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        account = authenticate(username=request.data.get('username', None), password=request.data.get('password', None))

        if account is not None:
            if account.is_active:
                login(request, account)
                token = AuthToken.objects.create(account)
                user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
                return Response({'token': token})
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
