from django.urls import path
# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import ReviewList, WatchListAV, WatchDetailAV, StreamPlatformAV, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]