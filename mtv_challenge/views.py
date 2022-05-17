from django.http import HttpRequest
from django.shortcuts import render


from star_fam_app.models import Character


def list_character(request):
    character = Character.objects.all()
    return render(request, "template.html", {"character": character})
