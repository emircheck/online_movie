from rest_framework.routers import DefaultRouter
from applications.review.views import ReviewViewSet, ReviewListView, ReviewDeleteView, ReviewUpdateView, \
    ReviewCreateView
from django.urls import path

router = DefaultRouter()
router.register('', ReviewViewSet)


urlpatterns = [
    path('create/', ReviewCreateView.as_view()),
    path('update/<int:pk>/', ReviewUpdateView.as_view()),
    path('delete/<int:pk>/', ReviewDeleteView.as_view()),
    path('list/', ReviewListView.as_view()),
]
urlpatterns.extend(router.urls)
