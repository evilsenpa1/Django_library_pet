from rest_framework import serializers
from .models import BookModel
from authors.models import AuthorModel

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AuthorModel.objects.all(),
    )

    class Meta:
        model = BookModel
        fields = '__all__'
        read_only_fields = ['pub_date']
