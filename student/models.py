from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse


#Multiple choice gender fields in tubles
Gender=(
    ("M","Male"),
    ('F',"Female"),
    ("O","Other")
)

#This class use to insert multiple course
class Courses(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Table for storing the data of student
class Student(models.Model):
    First_name=models.CharField(max_length=500)
    Last_name=models.CharField(max_length=500)
    Father_name=models.CharField(max_length=500)
    Mother_name=models.CharField(max_length=500)
    Date_of_birth=models.DateField()
    Email_id=models.EmailField(unique=True)
    Mobile_no=PhoneNumberField(null=False,blank=False)
    Admission_no = models.IntegerField(unique=True)
    Gender=models.CharField(choices=Gender,max_length=2)
    Address = models.CharField(max_length=150,)
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    countries = CountryField(multiple=False)
    City=models.CharField(max_length=50)
    slug=models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.First_name}"
    
    #A function for fetch the individual student record and it is use for editing purpose
    def get_absolute_url(self):
        return reverse ("school:edit",kwargs={"slug":self.slug}) 

     #A function for fetch the individual student record and it is use for deleting purpose   
    def delete_list(self):
        return reverse("school:delete",kwargs={"slug":self.slug})