"""

Forms
Generics in Django: forms.py

Django can also help streamline the form creation process for us!
We first need to create a file called forms.py which houses the general structure for any form we want in the application.
forms.py should be created in the base directory of the application. So for our program, the path should look:
vetoffice/forms.py.

Django forms are used with built-in generic classes to help build the forms in the template. => https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/
The code below will show a basic forms.py setup:
"""

from django import forms
from .models import User

class TestForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ("username")

"""
The first thing that needs to be done in forms.py is that we need to import forms from django and import any model we’ll be using from .models.
Then we can start constructing separate classes for each form we want to build.
In this example, we created a new class called TestForm.
TestForm takes in one parameter called forms.ModelForm which is used to help build these forms in the template.

Inside of the TestForm class is class Meta.
This inner Meta class is used to let the application know what is inside of the parent class.
Notice that we have two properties in the Meta class:

    model which tells the app what model we’ll be using
        In the example, we’re using the User model
    fields which can be a tuple or list that informs the app what fields to use
        In the example, we’re using one field, "username"

If we wanted to include every field of a model, instead of writing it all out inside of the fields list, we could include one string that says '__all__' to indicate that we want every field to be used.
Instructions
1.

In the previous exercises, we wrote in all the HTML for our forms.
But with generics, we don’t need to do that anymore.
We’ve removed the code from owner_create_form.html (that’s why the owner/create page is empty) and we’ll start the process of using form generics.

Create forms.py inside of vetoffice/.
Inside of forms.py, import forms from django and Owner from .models.

To create a new file: click on the 3 dots next to a folder to open up the menu for file creation

Inside of forms.py, there should just be two separate import statements at the top of forms.py
2.

Create a class called OwnerCreateForm that takes forms.ModelForm as a parameter.

Remember that this will look just like a normal Python class, it should have the parameter forms.ModelForm.
3.

Add the class Meta to the OwnerCreateForm class.

Remember that class Meta goes within the class of the form you are creating. Just like below:
"""
class ExampleFormClass(forms.ModelForm):
  class Meta:
    #...
"""
4.

Inside of Meta, make sure the model is set to Owner and the accepts the following fields: "first_name", "last_name", and "phone".
In a few more exercises we’ll be able to view this form.
Concept Review
Want to quickly review some of the concepts you’ve been learning?
Take a look at this material's cheatsheet!
https://www.codecademy.com/learn/paths/build-python-web-apps-with-django/tracks/forms-in-django/modules/django-forms/cheatsheet

"""
