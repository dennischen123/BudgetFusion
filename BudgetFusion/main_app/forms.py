from django.forms import ModelForm
from .models import Budget, Category, Expense


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ('name', 'total', 'length')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'date')