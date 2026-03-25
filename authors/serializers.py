from rest_framework import serializers
from .models import AuthorModel

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorModel
        fields = '__all__'
        read_only_fields = ['pub_date']
