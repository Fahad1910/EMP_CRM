from django.db import models


# Create your models here.


class Employees(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    contact=models.CharField(null=True,max_length=10,)
    profile_pic=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name   # for the object string representation
    

    