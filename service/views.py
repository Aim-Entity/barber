from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, "service/index.htm", context)
