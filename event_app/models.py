from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(max_length=100, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
