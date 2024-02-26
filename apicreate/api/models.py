from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phonenum = models.IntegerField()


