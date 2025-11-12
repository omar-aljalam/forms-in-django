from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favourite", views.AddFavouriteView.as_view()), # Put it before the int:pk (even tho it is int) so it does not get misunderstood as a primary key just to be safe
    path("reviews/<int:pk>", views.ReviewDetailsView.as_view())
]