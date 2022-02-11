from rest_framework import serializers

from account.models import Client


class GetAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'datetime_created',
            'datetime_updated',
            'uid',
            'name',
            'email',
            'is_superuser'
        ]


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

