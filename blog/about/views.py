from django.shortcuts import render


def about_author(request):
    return render(request, "about/about.html")


def tech(request):
    return render(request, "about/tech.html")
