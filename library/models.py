from django.db import models

# Create your models here.
'''
    ORM (object relational mapping)
    Python class -> Database table
    Class attributes python class -> columns inside the database table
    Objects of the python class -> records (tuples) inside the database table
'''
class Book(models.Model):
    # class attributes
    title = models.CharField(max_length=45)
    price = models.FloatField(null=True)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
