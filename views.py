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
  context = {"name": "<Put your name here>", "pets": pets}
  return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
  model = Owner

def OwnerCreate(request):
  if request.method == "POST":
    form = OwnerCreateForm(request.POST)
    # Add the form validation below:
    if form.is_valid():
      form = form.save()
  else:
    form = OwnerCreateForm()
  return render(request, "vetoffice/owner_create_form.html", {"form":form})
