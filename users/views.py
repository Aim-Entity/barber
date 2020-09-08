from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from home.models import Contact
from home.forms import ContactForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()

    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect("home")
    else:
        contact = ContactForm()

    context = {
        "form": form,
        "contact": contact
    }
    return render(request, "users/register.htm", context)
