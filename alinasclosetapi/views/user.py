from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers


class UserView(ViewSet):

    def list(self, request):
        user = User.objects.filter(is_superuser=False)

        
        serializer = UserSerializer(
            user, many=True, context={'request': request})
        return Response (serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'id']