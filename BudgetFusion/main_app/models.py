from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

LENGTH = (
    ('W', 'Week'),
    ('M', 'Month'),
    ('Y', 'Year')
)

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    length = models.CharField(
        max_length=1,
        choices=LENGTH,
        default=LENGTH[1][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - Total = {self.total}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    # total = models.IntegerField()
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('expense date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} added on {self.date}'






