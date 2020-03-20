from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

# #function for index(all budget)
# def budget_index(request):
#     pass

# #function for detail(single budget)
# def budget_detail(request, budget_id):
#     pass

# #function for create
# def budget_create(request):
#     pass

# #function for update
# def budget_update(request, budget_id):
#     pass

# #function for delete
# def budget_delete(request, budget_id):
#     pass
    # crud routes for Budget
    #route for index(all budget)
    path('budgets/', views.budget_index, name="budget_index"),
    #route for detail(single budget)
    path('budgets/<int:budget_id>/detail/', views.budget_detail, name="budget_detail"),
    #route for create
    path('budgets/create/', views.budget_create, name="budget_create"),
    #route for update
    path('budgets/<int:budget_id>/update/', views.budget_update, name="budget_update"),
    #route for delete
    path('budgets/<int:budget_id>/delete/', views.budget_delete, name="budget_delete"),


    # crud routes for Category
    #route for index(all Category)
    path('categories/', views.category_index, name="category_index"),
    #route for detail(single Category)
    path('categories/<int:category_id>/detail/', views.category_detail, name="category_detail"),
    #route for create
    path('categories/create/', views.category_create, name="category_create"),
    #route for update
    path('categories/<int:category_id>/update/', views.category_update, name="category_update"),
    #route for delete
    path('categories/<int:category_id>/delete/', views.category_delete, name="category_delete"),

    # crud routes for Expense
    #route for index(all Expense)
    path('expenses/', views.expense_index, name="expense_index"),
    
    #route for detail(single Expense)
    path('expenses/<int:expense_id>/detail/', views.expense_detail, name="expense_detail"),
    
    #route for create
    path('expenses/create/', views.expense_index, name="expense_create"),
    
    #route for update
    path('expenses/<int:expense_id>/update', views.expense_update, name="expense_update"),
    
    #route for delete
    path('expenses/<int:expense_id>/delete', views.expense_delete, name="expense_delete"),
]