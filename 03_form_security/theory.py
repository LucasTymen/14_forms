"""

    Forms
Form Security

When building any online form, proper defenses need to be made to protect the application from any malicious users.
This is because any form is susceptible to attacks including Cross Site Request Forgery attacks, or CSRF attacks.
These attacks happen when a user uses another user’s credentials without their knowledge and executes malicious actions.

Django has a built in method for defending against CSRF attacks by including a CSRF token. => https://docs.djangoproject.com/en/3.1/ref/csrf/
The CSRF token protects the application and the user by adding a secret token inside of the "POST" methods in the forms each time the form is rendered.
The CSRF token ensures that only the proper user is using the proper credentials.

The best way to add this token is to add a tag to the template inside of the <form> element:
"""

<form>
  {% csrf_token %}
</form>

"""
This token adds all the necessary security to help defend from possible CSRF attacks and is conventionally placed at the beginning of the form.

Form validation is also necessary to help defend out applications from possible attacks that use incorrect data types to cause problems, e.g. SQL attacks.
=>https://www.w3schools.com/sql/sql_injection.asp
This validation can include ensuring only specific data types are being submitted to protect our database.

Form validation is usually done in views.py in Django, and consists of an if statement before assigning data from the form to the database:
"""

if form.is_valid():
  form = form.save()

"""
Notice how Django makes it easy to secure our application!
Instructions
1.

Add a CSRF token to the under the opening <form> declaration like in the example given above.

This {% csrf_token %} token is a tag that goes inside of the <form> element.
2.

In views.py there is a method called OwnerCreate(request).
Inside of that method, locate the line form = OwnerCreateForm(request.POST) and add your validation below it and save the form if the form is valid.

Note: There is some extra code within this method that you may not recognize, but don’t worry, we’ll be covering this code later!

Make sure you add your code within the OwnerCreate() method.

To check if a form is valid use the .is_valid() method in a conditional. Then call .save() to save it:
"""

if form.is_valid():
  form = form.save()

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
