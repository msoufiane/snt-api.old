from django.contrib.auth import update_session_auth_hash
from authentication.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'username', 'date_joined', 'first_name','last_name', 'password', 'confirm_password', 'email')

        read_only_fields = ('created_at',)

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ProfilesListingField(serializers.RelatedField):
    def to_representation(self, value):
        profiles = ProfileSerializer(value)
        return profiles.data