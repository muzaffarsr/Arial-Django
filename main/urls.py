from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('control/manage/', views.manage, name='manage'),
    path('control/manage/categorys/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('search/', views.search, name='search'),
    path('leave-feedback/', views.leave_feedback, name='leave_feedback'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('customer/<product_id>/', views.customer, name='customer'),
    path('product/<product_id>/', views.product, name='product'),
    path('product-edit/<product_id>/', views.edit_product, name='edit-product'),
    path('category-edit/<category_id>/', views.edit_category, name='edit-category'),
    path('delete_category/<category_id>/', views.del_category, name='del_category'),
    path('delete_product/<product_id>/', views.del_product, name='del_product'),
    path('delete_feedback/<feedback_id>/', views.del_feedback, name='del_feedback'),
    path('category/<filter>/', views.filter, name='filter'),
]
