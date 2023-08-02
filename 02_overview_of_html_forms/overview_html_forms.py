"""

Forms
An Overview of HTML Forms

When a form is created in any HTML document, the <form> element is used to tell the application where the user input will come from.
This <form> element has two main attributes, action and method.
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form

action is used to tell the application what script to run when the form is submitted.
Most forms need an action attribute, but we don’t need it since Django handles the form submission for us.

method is used to tell the application where to submit the form data.
For Django, this attribute is optional and has two possible values, "POST" and "GET".
"POST" requests will send information to the server, while "GET" requests will retrieve information.
We’ll be using "POST" for form submission.

Inside of the <form> can be a number of different elements.
The two we’ll go over right now are the <input> and <label> elements. => https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label
The <label> element is used to add a label to the <input> element.
And the <input> element is where the user will input data for the form. => https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input

The <input> element has a number of optional attributes. Some of those being the id and name attributes.
The name attribute is used to help us grab the data from the form in our Django application.
The id attribute is used for identifying and referencing specific HTML elements.
This is usually used later for the for attribute value in a <label>.

An important attribute that is used with the <input> element is the type attribute.
This is used to tell the HTML document what data types to accept for input.
For instance, if we use the type "email", the form will not submit unless an email is typed into the input field.

Once all the necessary input elements are added to the form, one more <input> element is needed that is of type "submit".
This will create a button that lets the user send their data to the application once all of the fields are filled out.

There’s a lot more that we can explore for HTML forms, but we’ll see later on how Django takes care of some of this work for us.
Instructions
1.

Create a <form> element to the HTML document currently open (owner_create_form.html). Set the action to "" and the method to "POST".

Remember that the <form> element should look like the one here.
"""
<form action="" method="POST">

</form>
"""
2.

Inside of <form>, create a <label> element with:

    a name attribute set as "LabelField",
    a for attribute set as "InputField".
    the text of the <label> to Owner name:.

When the <label> element is finished, it should look roughly like this:
"""
...
<label name="labelName" for="referenceName">Label Text</label>
...
"""
3.

Add the <input> element after the <label> element. Set both name and id as "InputField".

Remember that the <input> field should follow this structure:
"""
...
<input id="NameOfInput" name="NameOfInput"/>
...
"""
4.

At the bottom of the form, add an <input> with type as "submit" that also has a value of "Submit".

A basic submit button with custom text should look like this:
"""
<input type="submit" value="Custom text goes here" />
"""
"""
