"""

Forms
Generics in Django: Paths & Templates

Once the class is created in views.py, a path needs to be added to urls.py so that the template can be rendered.
The following path() syntax should look familiar:
"""

path("path/name", views.TestFormCreate.as_view(), name="testformcreate"),

"""
Now we can actually create the template that will house the form.
This template will just be a normal template and will be stored with all the other templates.
The file path should look like this:

appname/
├─ manage.py
└─ mysite/
    └─ templates
        └─ mysite/
            └─ form_template.html


This template will be treated as a normal template, meaning that it will usually extend from base.html and include blocks.
Inside of the content blocks will be the following code.
"""

{% extends "appname/base.html" %}

{% block content %}
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Submit"/>
</form>
{% endblock %}

"""
This code looks very similar to a normal HTML form, including the form element with the method being "POST", a csrf_token, and an <input> element of type "submit".
However, the entirety of the form is inside of the variable tag, using form.as_p.
Conveniently, form.as_p tells the DTL to render all of the fields we included as form inputs neatly inside <p> elements.
Instructions
1.

The owner/create page still isn’t rendering correctly, so let’s start to change that.

Inside of urls.py, add a path to "owner/create" with the view OwnerCreate.as_view(). Set the name to "ownercreate".

Remember that a path should look like the one here,
"""

path("pet/details", views.PetDetail.as_view(), name="petdetails")

"""
2.

Let’s set up our template now:

    Create a template in templates/vetoffice/ called owner_create_form.html.
    Inside of this template, have it extend from vetoffice/base.html.
    Add a block named content. Make sure to end the block as well.

Don’t forget that to extend from a base template, and to open a block, you use the following code:
"""

{% extends "base.html" %}

{% block content %}

"""
3.

Inside of the content block, add the elements necessary to build the HTML form using Django, including:

    The <form>.
    The {% csrf_token %}
    The <input> of type "submit".

The <form> element should include an attribute that sets the method to "POST", and the <input> should have the attribute type set to "submit".
4.

Notice our form is starting to take shape, let’s add in the rest.

We need to add {{ form.as_p }} inside the <form>.

Then run your code to see the finished form rendered in the mini-browser!
If you try submitting something, you’ll get an error about redirecting — we’ll fix that in the next exercise.

If the page isn’t displaying anything, refresh the mini-browser
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
