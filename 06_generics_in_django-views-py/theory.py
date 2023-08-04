"""

Forms
Generics in Django: views.py

Now that we have the form made in forms.py, we can wire up our views.py classes to render our templates.
Remember we’ll need to import both our form and our generic views:
=> https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/
"""

from .forms import TestForm
from django.views.generic.edit import CreateView

"""
Recall that we had to create a class for TestForm in views.py.
This class is usually named after the form, followed by the type of view being created.
For instance, with our TestForm, we would make a new class that’s called TestFormCreate that takes in CreateView.
A sample of this class is below.
"""

class TestFormCreate(CreateView):
  model = TestModel
  template_name = "appName/form_template.html"
  form_class = TestForm

"""
This class has three properties as seen above, those being the model, the template_name, and the form_class.
The model is assigned the model we want to use. The template_name is the template file that we want the form to be used in.
And the form_class is going to be the class that we created in forms.py.
The form_class will also tell Django to use this form within the template when building the form for us.
Instructions
1.

Remember that we need to tell views.py what we are going to be using, which means that we need to add imports for:

    the generic view, CreateView from django.views.generic.edit
    the form that we just made: OwnerCreateForm from .forms

2.

Create the OwnerCreate class.
3.

Now that we have a place to put our creation form, let’s add everything we need to the OwnerCreate class by:

    Having the model set as Owner.
    Having the template_name set as "vetoffice/owner_create_form.html".
    Having the form_class set as OwnerCreateForm.

Note: the owner/create page is still blank, but we’re really close to rendering the form!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
