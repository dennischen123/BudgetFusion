import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Budget, Category, Expense
from .forms import BudgetForm, CategoryForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# api views
@login_required
def api(request, user_id, budget_id):
    budgets = Budget.objects.filter(user_id=user_id)
    budget = Budget.objects.get(id=budget_id)
    categories = list(budget.category_set.values())
    expenses = Expense.objects.filter(category__budget_id=budget_id)
    expenses_json = list(expenses.values())
    print(f'expenses = {expenses}')
    print(f'expenses_json = {expenses_json}')

    expenses_total = 0
    for expense in expenses:
        expenses_total += expense.amount
    budgets_json = list(budgets.values())
    return JsonResponse({'categories': categories,'budget_name' : budget.name ,'budget_total': budget.total, 'expense_total' : expenses_total, 'budgets' : budgets_json}, safe=False)

@login_required
def reports(request, user_id):
    budgets = Budget.objects.filter(user_id=user_id)
    print(budgets)
    return render(request, 'reports/reports.html', {'budgets': budgets})


# crud functions for Budget ###
###########################################################
@login_required
def budget_index(request):
    budgets = Budget.objects.all()
    return render(request, 'budgets/index.html', { 'budgets' : budgets})


@login_required
def budget_detail(request, budget_id):
    budgets = Budget.objects.all()
    budget = Budget.objects.get(id=budget_id)
    budget_form = BudgetForm()
    category_form = CategoryForm()
    expense_form = ExpenseForm()
    return render(request, 'budgets/details.html', { 
        'budget' : budget,
        'budgets' : budgets,
        'budget_form' : budget_form,
        'category_form' : category_form,
        'expense_form' : expense_form,
        })


@login_required
def budget_create(request):
    if request.method == 'POST':
        budget_form = BudgetForm(request.POST)
        if budget_form.is_valid():
            budget = budget_form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_index')
    else:
        budget_form = BudgetForm()
    return render(request, 'budgets/budget_form.html', {'budget_form' : budget_form})

@login_required
def budget_update(request, budget_id):
    budget = Budget.objects.get(id=budget_id)

    if request.method == "POST":
        budget_form = BudgetForm(request.POST, instance=budget)
        if budget_form.is_valid():
            budget = budget_form.save()
            return redirect('budget_index')
    else:
        budget_form = BudgetForm(instance=budget)
    return render(request, 'budgets/budget_form.html', { 'budget_form' : budget_form })

@login_required
def budget_delete(request, budget_id):
    return Budget.objects.get(id=budget_id).delete() and redirect('budget_index')


    # crud functions for Category ##
###########################################################
@login_required
def category_index(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    categories = Category.objects.filter(budget_id=budget_id)
    return render(request, 'categories/category_list.html', { 'categories': categories, 'budget' : budget, 'budget_id' : budget.id })

    
@login_required
def category_detail(request, budget_id, category_id):
    pass

@login_required
def category_create(request, budget_id):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.budget_id = budget_id
            category.save()
        return redirect('category_index', budget_id)
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', { 'form' : form})

@login_required
def category_update(request, budget_id, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_index', budget_id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', { 'form' : form})

@login_required
def category_delete(request, budget_id, category_id):
    return Category.objects.get(id=category_id).delete() and redirect('category_index', budget_id)


    # crud functions for Expense ##
###########################################################

@login_required
def expense_index(request, budget_id, category_id):
    categories = Category.objects.filter(budget_id=budget_id)
    expenses = Expense.objects.filter(category_id=category_id)
    return render(request, 'categories/category_details.html', { 'expenses' : expenses,'categories' : categories, 'category_id' :category_id, 'budget_id' : budget_id})

@login_required
def expense_detail(request, budget_id, category_id, expense_id):
    pass

@login_required
def expense_create(request, budget_id, category_id):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            return redirect('expense_index', budget_id, category_id)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', { 'form': form})
            
@login_required
def expense_update(request, budget_id, category_id, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            return redirect('expense_index', budget_id, category_id)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', { 'form': form})

@login_required
def expense_delete(request, budget_id, category_id, expense_id):
    return Expense.objects.get(id=expense_id).delete() and redirect('expense_index', budget_id, category_id)


########## sign up #############
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('budget_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form' : form, 'error_message' : error_message})