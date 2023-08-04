"""

Forms
Redirecting

After a user submits their data, they should be redirected to another page.
Otherwise, the user might resubmit data again and create duplicates.
The Django convention is to create a .get_absolute_url() method.

The .get_absolute_url() method goes inside of models.py and inside of the class of the model that the form is using.
For instance, if we had used a model called TestModel in our forms, the TestModel class would look like this in models.py:
"""

class TestModel(models.Model):
  field1 = models.CharField()
  field2 = models.CharField()

  def get_absolute_url(self):
    return "list"

"""
The method get_absolute_url() has one parameter, self, and the method is used to direct users to a specific path.
Notice that we have the method returning a string, which is the relative path name.
This string tells Django where to redirect our users to after submitting their form.
In the case described above, the users will be redirected to the "model/list" path even though we’re only returning "list" —
that’s because Django is configured to assume we want to send users somewhere related to the model.

By adding one method, Django lowers the chance of our users re-submitting a form, or wondering if their information got sent!
Instructions
1.

Inside of models.py, locate the Owner model. Then add the .get_absolute_url() method and have it return "list"

After you’re done, try out the form!

Remember that .get_absolute_url() takes in one parameter called self.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
