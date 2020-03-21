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
def category_index(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    categories = Category.objects.filter(budget_id=budget_id)
    return render(request, 'categories/index.html', { 'categories': categories, 'budget' : budget })

    
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
    context = {
        'expenses' : expenses,
        'categories' : categories
    }
    return render(request, 'categories/details.html', {context})


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