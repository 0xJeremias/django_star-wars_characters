from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthdate = models.DateField()
    num_id = models.IntegerField()
