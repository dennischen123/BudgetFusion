from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Budget, Category, Expense
from .forms import BudgetForm, CategoryForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

# crud functions for Budget ###
###########################################################
#function for index(all budget)
def budget_index(request):
    budgets = Budget.objects.all()
    return render(request, 'budgets/index.html', { 'budgets' : budgets})

#function for detail(single budget)
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


#function for create
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

#function for update
def budget_update(request, budget_id):
    budget = Budget.objects.get(id=budget_id)

    if request.method == "POST":
        budget_form = BudgetForm(request.POST)
        if budget_form.is_valid():
            budget = budget_form.save()
            return redirect('budget_index')
    else:
        budget_form = BudgetForm(instance=budget)
    return render(request, 'budgets/budget_form.html', { 'budget_form' : budget_form })

#function for delete
def budget_delete(request, budget_id):
    return Budget.objects.get(id=budget_id).delete() and redirect('budget_index')


    # crud functions for Category ##
###########################################################
#function for index(all Category)
def category_index(request):
    pass

# function for detail(single Category)
def category_detail(request, category_id):
    pass

# function for create
def category_create(request):
    pass

# function for update
def category_update(request, update_id):
    pass

# function for delete
def category_delete(request, delete_id):
    pass


    # path('budgets/<int:budget_id>/expenses/', views.expense_index, name="expense_index"),
    # path('budgets/<int:budget_id/expenses/<int:expense_id>/detail/', views.expense_detail, name="expense_detail"),
    # path('budgets/<int:budget_id/expenses/create/', views.expense_index, name="expense_create"),
    # path('budgets/<int:budget_id/expenses/<int:expense_id>/update', views.expense_update, name="expense_update"),
    # path('budgets/<int:budget_id/expenses/<int:expense_id>/delete', views.expense_delete, name="expense_delete"),
    # crud functions for Expense ##
###########################################################
#function for index(all Expense)

def expense_index(request):
    expenses 

#function for detail(single Expense)
def expense_detail(request, expense_id):
    pass

#function for create
def expense_create(request):
    pass

#function for update
def expense_update(request, expense_id):
    pass

#function for delete
def expense_delete(request, expense_id):
    pass




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