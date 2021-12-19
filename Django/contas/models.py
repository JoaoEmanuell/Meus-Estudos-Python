from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    dt_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Transation(models.Model):
    date = models.DateField()
    describe = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transations'

    def __str__(self):
        return self.describe