from django.db import connections
from django.db import models

# Create your models here.

class admin_detailss(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def _str_(self):
        return self.name

class book_detailss(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=25)
    book_name = models.CharField(max_length=200)
    author_name=models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
