from .models import Book

from rest_framework import viewsets
from .serializers import BookSerializer


""" API Views """

class BooksViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
