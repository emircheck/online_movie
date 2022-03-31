from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from applications.account.serializers import ProfileSerializer
from applications.movies.models import Movie
from applications.account.models import Profile
from applications.movies.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', ]

    def get_serializer_context(self):
        return {'request': self.request}


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSearch(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


class MovieFilter(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre')
        if genre is not None:
            queryset = queryset.filter(genre=genre)
        return queryset


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        profile = Profile.objects.get(user=request.user.id)
        if profile.favorite.filter(id=pk).exists():
            profile.favorite.set(profile.favorite.exclude(id=pk))
            msg = 'Movie was deleted from favorites!'
        else:
            profile.favorite.add(pk)
            profile.save()
            msg = 'Movie added to favorite successfully!'
        return Response(msg, status=status.HTTP_200_OK)


class FavoriteListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
