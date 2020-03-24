import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Budget, Category, Expense
from .forms import BudgetForm, CategoryForm, ExpenseForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Users -> Budget -> Category -> expense
# need budget_name,budget_total and  Total of all expense amount
def api(request, user_id, budget_id):
    budgets = Budget.objects.filter(user_id=user_id)
    budget = Budget.objects.get(id=budget_id)
    expenses = Expense.objects.filter(category__budget_id=budget_id)
    expenses_json = list(expenses.values())
    # budget_json = list(budget.values())
    expenses_total = 0
    for expense in expenses:
        expenses_total += expense.amount
    budgets_json = list(budgets.values())
    return JsonResponse({'budget_name' : budget.name ,'budget_total': budget.total, 'expense_total' : expenses_total, 'budgets' : budgets_json}, safe=False)

## reports testing start #############
    #testing only
def reports(request, user_id):
    budgets = Budget.objects.filter(user_id=user_id)
    print(budgets)
    return render(request, 'reports/reports.html', {'budgets': budgets})

#actual reports function
def reports_detail(request, budget_id):
    categories = Category.objects.filter(budget_id=budget_id)
    context = {

    }
    return render(request, 'reports/reports.html', {context})
#### reports testing ends #######################

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
        budget_form = BudgetForm(request.POST, instance=budget)
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
def category_index(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    categories = Category.objects.filter(budget_id=budget_id)
    return render(request, 'categories/category_list.html', { 'categories': categories, 'budget' : budget, 'budget_id' : budget_id })

    
# function for detail(single Category)
def category_detail(request, budget_id, category_id):
    pass


# function for create
def category_create(request, budget_id, category_id):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            return redirect('category_index', budget_id)
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', { 'form' : form})

# function for update
def category_update(request, budget_id, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_index', budget_id, category_id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', { 'form' : form})

# function for delete
def category_delete(request, budget_id, category_id):
    return Category.objects.get(id=category_id).delete() and redirect('category_index', budget_id)


    # crud functions for Expense ##
###########################################################
#function for index(all Expense)

#index all expense for a category of a budget
def expense_index(request, budget_id, category_id):
    categories = Category.objects.filter(budget_id=budget_id)
    expenses = Expense.objects.filter(category_id=category_id)
    return render(request, 'categories/category_details.html', { 'expenses' : expenses,'categories' : categories, 'category_id' :category_id, 'budget_id' : budget_id})


#function for detail(single Expense)
def expense_detail(request, budget_id, category_id, expense_id):
    pass

#function for create
def expense_create(request, budget_id, category_id):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            return redirect('expense_index', budget_id, category_id)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', { 'form': form})
            

#function for update
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



#function for delete
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