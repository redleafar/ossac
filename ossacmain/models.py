from django.db import models

# Create your models here.

class Installation(models.Model):
    STATUS = (
        ('good', ('En buen estado')),
        ('medium', ('Algo está ocurriendo')),
        ('bad', ('Defectuoso'))
    )

    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 100)
    detail = models.CharField(max_length = 500)
    status = models.CharField(max_length = 100, choices = STATUS,  default = "good")
