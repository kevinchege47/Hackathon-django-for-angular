from django.db import models

# Create your models here.
class Doctor(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    
    )

    physicianID = models.CharField(max_length=10,primary_key=True,default= '0000',null=False)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True,choices=GENDER)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.first_name


class Allergies(models.Model):
    allergy_name = models.CharField(max_length=50)

    def __str__(self):
        return self.allergy_name

class illnesses(models.Model):
    illness_name = models.CharField(max_length=50)

    def __str__(self):
        return self.illness_name

class Patient(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        

    )

    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    bloodgroup = models.CharField(max_length=50,null=True)
    age = models.CharField(max_length=50,null=True)
    ID_number = models.CharField(max_length=10,default = '00000')
    phone = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True,choices =GENDER)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    allergies = models.ManyToManyField(Allergies,blank=True)
    illnesses = models.ManyToManyField(illnesses,blank=True)

    def __str__(self):
        return self.first_name

