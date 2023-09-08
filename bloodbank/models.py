from django.db import models

# Create your models here.
from django.db import models

class BloodDonor(models.Model):
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
