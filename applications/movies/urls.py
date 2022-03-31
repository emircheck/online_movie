from django.urls import path
from applications.movies.views import MovieListView, MovieDetailView, MovieFilter, MovieSearch, FavoriteView, \
    FavoriteListView

urlpatterns = [
    path('', MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
    path('search/', MovieSearch.as_view),
    path('filter/', MovieFilter.as_view()),
    path('<int:pk>/favorite/', FavoriteView.as_view()),
    path('favorites/', FavoriteListView.as_view()),
]
