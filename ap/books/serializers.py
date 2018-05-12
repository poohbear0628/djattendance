from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(ModelSerializer):
  fields = '__all__'

  class Meta:
    model = Book
