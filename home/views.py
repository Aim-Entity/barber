from django.shortcuts import render, redirect
from home.models import Contact, Testimonial
from home.forms import ContactForm


def index(request):
    testimonial = Testimonial.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "tests": testimonial
    }
    return render(request, 'home/index.htm', context)
