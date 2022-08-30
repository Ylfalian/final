from urllib import request
from django.shortcuts import render
from .models import juego


def home(request):
    Juego = juego.objects.all()
    return render(request, "home.html",{"Juego": Juego})
