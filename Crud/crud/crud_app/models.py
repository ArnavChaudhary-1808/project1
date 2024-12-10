# crud_app/models.py
from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
