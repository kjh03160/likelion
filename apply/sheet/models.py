from django.db import models
from django.contrib.auth.models import User
from django.db.models import (Model, TextField, DateTimeField, ForeignKey,
                              CASCADE)
# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name='user')
    GENDER = (
        ('F','female'),
        ('M','male'),
    )
    name = models.CharField(max_length=100, null=False)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1,choices = GENDER)
    major = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.user.username