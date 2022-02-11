from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from account import serializers


class AuthTestView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        return Response(status=status.HTTP_200_OK)


class GetAccountView(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetAccountSerializer

    def get_object(self):
        return self.request.user
