from django.db import models


class Port(models.Model):
    name = models.TextField()
    rating = models.IntegerField()


class Boat(models.Model):
    name = models.TextField()
    cabins = models.IntegerField()
    port = models.ForeignKey(Port, on_delete=models.PROTECT)
