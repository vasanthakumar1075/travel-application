from django.db import models

# Create your models here.

class FormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    destination = models.CharField(max_length=255)
    travelers = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name

