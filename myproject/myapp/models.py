from django.db import models

class Newswrite(models.Model):
    heading = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    summary = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.heading

class Sports(models.Model):
     heading = models.CharField(max_length=100)
     photo = models.ImageField(upload_to='photos/')
     summary = models.CharField(max_length=200)
     description = models.TextField()
     author = models.CharField(max_length=50)
     date = models.DateTimeField()

     def __str__(self):
         return self.heading
     
class Technology(models.Model):
    heading = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    summary = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.heading
class Breaking(models.Model):
    heading = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    summary = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.heading



