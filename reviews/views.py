from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic import View

from .froms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    # fields = "__all__" # we can remove RviewView entierly
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data

class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context

class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        # request.session["favourite_review"] = fav_review # Serilization Error because fav_review is an object -- Store simple values in a session -- No Complex values nor Objects! Keep it simple
        request.session["favourite_review"] = review_id # STRING
        return HttpResponseRedirect("/reviews/" + review_id)
