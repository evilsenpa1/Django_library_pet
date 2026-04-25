from rest_framework import serializers
from django.contrib.auth.models import User as UserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    last_login = serializers.DateTimeField(read_only=True, allow_null=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "password", "last_login", "date_joined"]

    def create(self, validated_data):
        # create_user calls set_password() internally
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
