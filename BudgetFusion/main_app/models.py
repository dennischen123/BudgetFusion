from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

LENGTH = (
    ('Week', 'Week'),
    ('Month', 'Month'),
    ('Year', 'Year')
)


# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    length = models.CharField(
        max_length=5,
        choices=LENGTH,
        default=LENGTH[1][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - Total = {self.total}'
    
    def get_categories(self):
        return Category.objects.filter(budget_id=self.id)
    
    def get_expenses(self, category):
        return Expense.objects.filter(category_id=category.id)

class Category(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_expenses(self):
        return Expense.objects.filter(category_id=self.id)
    


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    date = models.DateField('expense date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} added on {self.date}'






