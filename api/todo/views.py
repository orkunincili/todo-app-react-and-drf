from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, filters
from todo import serializers, models



class TodoViewSet(viewsets.ModelViewSet):

    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
