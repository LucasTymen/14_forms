"""
Form Redirections

from .models import Model_Name
 """
def renderTemplate(request):
  if request.method == 'POST':
    test_model = new Model_Name()
    test_model.field = request.POST[""field_from_html""]
    test_model.save()
    return render(request, 'submit_success.html')
  return render(request, 'template_name.html'
"""
Users can be redirected to a success page after form submission to reduce the chances of a form being submitted more than once.
"""


"""
Using Form Data for Models
"""
from .models import Model_Name

def renderTemplate(request):
  if request.method == "POST":
    test_model = new Model_Name()
    test_model.field = request.POST["field_from_html"]
    test_model.save()
  return render(request, 'template_name.html')
"""
The model must be imported into views.py in order to manipulate or create a model instance.
"""


"""
Form Attributes
The <form>‘s action attribute should be set as "" and the method set as "POST". There must be an input type of "submit" included in the <form> tags.

"""
{% block exemple %}
<form action="" method="POST">
   <input id="your_input" type="text" name="your_input" value="{{ current_input }}">
  <input type="submit" value="OK">
</form>
{% endblock %}
"""

Forms
Django uses forms are used to get user input and works similarly to HTML forms.
"""

<form action=""""q< method=""POST"">
  <input id=""your_input"" type=""text"" name=""your_input"" value=""{{ current_input }}"">
  <input type=""submit"" value=""OK"">
</form>



Forms Class
Class properties must be assigned to a field from forms.

"""
from django import forms

class TestForm(forms.ModelForm):
  class Meta:
    model = Test
