from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # testing
    path('reports/', views.reports, name='reports'),
    # api route for report
    path('api/reports/budgets/<int:budget_id>/categories/<int:category_id>/expenses/', views.reports_detail, name="reports_detail"),

    # crud routes for Budget
    path('budgets/', views.budget_index, name="budget_index"),
    path('budgets/<int:budget_id>/detail/', views.budget_detail, name="budget_detail"),
    path('budgets/create/', views.budget_create, name="budget_create"),
    path('budgets/<int:budget_id>/update/', views.budget_update, name="budget_update"),
    path('budgets/<int:budget_id>/delete/', views.budget_delete, name="budget_delete"),

    # crud routes for Category
    path('budgets/<int:budget_id>/categories/', views.category_index, name="category_index"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/detail/', views.category_detail, name="category_detail"),
    path('budgets/<int:budget_id>/categories/create/', views.category_create, name="category_create"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/update/', views.category_update, name="category_update"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/delete/', views.category_delete, name="category_delete"),

    # crud routes for Expense
    path('budgets/<int:budget_id>/categories/<int:category_id>/expenses/', views.expense_index, name="expense_index"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/expenses/<int:expense_id>/detail/', views.expense_detail, name="expense_detail"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/expenses/create/', views.expense_index, name="expense_create"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/expenses/<int:expense_id>/update', views.expense_update, name="expense_update"),
    path('budgets/<int:budget_id>/categories/<int:category_id>/expenses/<int:expense_id>/delete', views.expense_delete, name="expense_delete"),

    path('accounts/signup', views.signup, name='signup'),
]