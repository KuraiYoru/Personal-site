from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def team(request):
    return render(request, 'portfolio/team.html')


def taekwondo(request):
    return render(request, 'portfolio/taekwondo.html')


def programming(request):
    return render(request, 'portfolio/programming.html')
