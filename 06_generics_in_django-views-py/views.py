from django.shortcuts import render
from django.views.generic import ListView
from .models import Owner
# Add your imports below:


def home(request):
   context = {"name": "Djangover"}
   return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
   model = Owner

# Add your class below:
