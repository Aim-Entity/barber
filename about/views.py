from django.shortcuts import render, redirect
from home.models import Contact
from home.forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "form": form
    }
    return render(request, "about/index.htm", context)
