from django.shortcuts import render
from django.views.generic import ListView
from .models import Owner
# Add your imports below:
from django.views.generic.edit import CreateView
from .forms import OwnerCreateForm

def home(request):
   context = {"name": "Djangover"}
   return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
   model = Owner

# Add your class below:
class OwnerCreate(CreateView):
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  form_class = OwnerCreateForm
