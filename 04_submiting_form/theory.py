"""

Forms
Submitting a Form

In Django, we’ll be using the "POST" method when the form is submitted, which means all of the data from the forms will be sent to the POST method in views.py.

Before we go into accessing the POST data, we need to understand that the logic is stored in the same function in views.py that renders the template.
Therefore, to differentiate how the view function should treat a POST request vs rendering the usual form, we use an if statement.
This if statement checks that the request method is "POST".
Here’s an example for how to structure our view function that handles the rendering logic:
"""

from .models import Model_Name

def renderTemplate(request):
  if request.method == "POST":
    test_model = Model_Name()
    test_model.field = request.POST["field_name"]
    test_model.save()
  return render(request, "template_with_form.html")

"""
The first thing that needs to be done is to check if the request.method is equal to "POST".
When the method is "POST", it means that the form was submitted which means that we can grab all the data and use it to create a new model instance.
Notice our test_model is a new Model_Name(). We then assign the test_model.field a value of request.POST["field_name"].
This is because in our form, we had an input field with a name set to "field_name".
The request.POST["field_name"] syntax shows that request is treated like a dictionary with a "field_name" property.
Once all of the data from request.POST is added to the model, we can save the model and render the form again.

If our conditional isn’t met, it usually means that the form is being rendered for the first time, so we can skip the instance creation and just render the form as normal.

Aside from re-rendering the template, we could also redirect to a new template! We’ll discuss redirecting in more detail later.
Instructions
1.

In views.py, locate the method OwnerCreate() and add an if statement to check if the request method is "POST".

Don’t forget that to check the request method you need to call request.method.
2.

If the method is "POST", create a new instance called newOwner using the Owner model.

Don’t forget that the instance should be assigned to a model, you don’t need to add any arguments.
For instance, if we were using TestModelName, it would look like below:
"""
testModelInstance = TestModelName()
"""
3.

Access "first_name" from POST and assign it to newOwner.first_name.
Do the same thing for last_name and phone_number.
Once that’s done, save the model.

Remember that POST is treated like a dictionary, and is called using request.POST.
Concept Review
Want to quickly review some of the concepts you’ve been learning?
Take a look at this material's cheatsheet!

"""
