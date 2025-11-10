from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flock(models.Model):
    FLOCK_TYPES = [
        ('layers', 'Layers'),
        ('broilers', 'Broilers'),
        ('others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flocks')
    name = models.CharField(max_length=100)
    flock_type = models.CharField(max_length=25, choices=FLOCK_TYPES)
    number_of_birds = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    age = models.PositiveIntegerField(help_text="Age in Days")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.CharField(max_length=100)
    housing = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    # keep track of active flocks
    is_active = models.BooleanField(default=True)

    # keep track of total hens broilers/layers

    def __str__(self):
        return self.name