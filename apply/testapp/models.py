from django.db import models

class Apply(models, Model):
    HTML = (
        ('Y', 'yes')
        ('N', 'no')
    )
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    q5 = models.TextField()
    codecademy = models.TextField(max_length=1, choices=HTML)
    