from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    pass

# crud functions for Budget ###
###########################################################
#function for index(all budget)
def budget_index(request):
    pass

#function for detail(single budget)
def budget_detail(request, budget_id):
    pass

#function for create
def budget_create(request):
    pass

#function for update
def budget_update(request, budget_id):
    pass

#function for delete
def budget_delete(request, budget_id):
    pass


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



    # crud functions for Expense ##
###########################################################
#function for index(all Expense)

def expense_index(request):
    pass

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