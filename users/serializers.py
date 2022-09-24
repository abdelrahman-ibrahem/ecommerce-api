from rest_framework import serializers
from django.contrib.auth import get_user_model


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
                'username', 'email', 'photo',
                'first_name', 'last_name'
            ]