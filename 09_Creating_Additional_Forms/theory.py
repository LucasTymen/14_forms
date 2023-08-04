"""

Forms
Creating Additional Forms

When creating more forms for the Django application, they should all be included inside of forms.py.
For that reason, we need to make sure that forms.py does not become too disorganized.
We recommend keeping as much relative data together and as close as possible.
Try to keep the code as clean as possible when writing a new form.
This can be done by keeping all information as close together as possible and commenting on the code as you write it.
Also, try not to add anything that isn’t necessary.

With the methods used in this lesson, forms.py should not become too large to handle.
Even though larger application might have larger forms.py the overall length should not have an impact on application performance.
Instructions
1.

We did some setup in models.py, views.py, urls.py, and created both vetoffice/templates/patient_list.html and vetoffice/templates/patient_create_form.html.
But, the patient/create page doesn’t load! That’s because forms.py still needs come configuration.

Import another model called Patient into forms.py

This should be done on the same line as the Owner import by adding a comma after Owner then adding Patient. For instance:
"""

from .models import Model_Name_One, Model_Name_Two

"""
2.

Now you can add a new form called PatientCreateForm.
This form should use the model Patient and have the fields: "pet_name", "animal_type", "breed", "age", and "owner".

Click on the “Add Patient” button to see your new form!

Patient should be assigned to model and the fields should be a dictionary assigned to fields.
This should all go inside of class Meta:.
Also, remember that the form class itself takes one parameter called forms.ModelForm.


"""
