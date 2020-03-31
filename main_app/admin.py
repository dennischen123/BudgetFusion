from django.contrib import admin
from .models import Budget, Category, Expense
# Register your models here.

admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Expense)
