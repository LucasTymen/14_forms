from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Owner
from .forms import OwnerCreateForm

pets = [
   { "petname": "Fido", "animal_type": "dog"},
   { "petname": "Clementine", "animal_type": "cat"},
   { "petname": "Cleo", "animal_type": "cat"},
   { "petname": "Oreo", "animal_type": "dog"},
]

def home(request):
   context = {"name": "Djangoer", "pets": pets}
   return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
   model = Owner

def OwnerCreate(request):
  # Add your code below:
  if request.method == "POST":
    newOwner = Owner()
    newOwner.first_name = request.POST["first_name"]
    newOwner.last_name = request.POST["last_name"]
    newOwner.phone_number = request.POST["phone_number"]
    newOwner.save()
  return render(request, "vetoffice/owner_create_form.html")
