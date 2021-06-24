from django.db import models


# Create your models here.

class Flower(models.Model):
    """Flower model with required fields"""
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    classification = models.CharField(max_length=33,blank=True)

    def __str__(self):
        return str(self.classification)
