# users/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UsersSerializers
from rest_framework import status
from .forms import UpdateUserInformation


# get current user
User = get_user_model()
class CurrentUser(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    model = User
    serializer_class = UsersSerializers

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfile(generics.RetrieveUpdateAPIView):
    model = User
    serializer_class = UsersSerializers

    def get_object(self):
        user = self.request.user
        return user
    
    def retrieve(self, request, *args, **kwargs):
        serializer = UsersSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() and request.user == self.object:
            self.object.phone = request.data.get('phone', self.object.phone)
            self.object.first_name = request.data.get(
                'first_name', self.object.first_name)
            self.object.last_name = request.data.get(
                'last_name', self.object.last_name)
            self.object.photo = request.data.get(
                'photo', self.object.photo)

            self.object.save()
            return Response(UsersSerializers(self.object, context=self.get_serializer_context()).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


