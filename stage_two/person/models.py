from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, validators=[alphanumeric])
    # Add other fields as needed

    def __str__(self):
        return self.name