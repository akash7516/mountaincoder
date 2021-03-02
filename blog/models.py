from django.db import models

# Create your models here.

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content=models.TextField()
    short_desc=models.CharField(max_length=300,default="")
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    

class Contact(models.Model):
   
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    desc=models.TextField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Signup(models.Model):
   
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



