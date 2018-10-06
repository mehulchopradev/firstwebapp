from django.db import models

# Create your models here.
'''
    ORM (object relational mapping)
    Python class -> Database table
    Class attributes python class -> columns inside the database table
    Objects of the python class -> records (tuples) inside the database table
'''

class PublicationHouse(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    # class attributes
    title = models.CharField(max_length=45)
    price = models.FloatField(null=True)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=50, null=True)
    noofcopies = models.IntegerField(default=0)
    publicationhouse = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class Review(models.Model):
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    country = models.CharField(max_length=20)
    booksissued = models.ManyToManyField(Book)

    def __str__(self):
        return self.username
