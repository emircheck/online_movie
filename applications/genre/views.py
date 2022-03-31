from rest_framework import generics
from applications.genre.models import Genre
from applications.genre.serializers import GenreSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
