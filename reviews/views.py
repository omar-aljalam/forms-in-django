from django.shortcuts import render
from django.http import HttpResponseRedirect
from .froms import ReviewForm
# Create your views here.

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST) # Pass instance to check for existing data in case of updating

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")