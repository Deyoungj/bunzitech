from django.shortcuts import render


def home(request):
    return render(request, 'bunzitech_app/home.html')
