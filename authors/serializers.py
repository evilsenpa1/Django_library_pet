from rest_framework import serializers
from .models import AuthorModel

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorModel
        fields = ["id", "name", "date_of_birth", "pub_date", "books"]
        read_only_fields = ["pub_date"]
