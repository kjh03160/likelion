from django.db import models
from django.contrib.auth.models import User
from sheet.models import Signup

class Apply(models.Model):
    user = models.ForeignKey(User, related_name='apply_user',on_delete=models.CASCADE)
    HTML = (
        ('Y', 'yes'),
        ('N', 'no')
    )
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    q5 = models.TextField()
    codecademy = models.TextField(max_length=1, choices=HTML)
    