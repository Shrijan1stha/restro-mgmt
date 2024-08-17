from django.urls import path
from .views import home, table_list, create_table, edit_table, delete_table, menu, create_menu, delete_menu, edit_menu, category, create_category, edit_category, delete_category, order, create_order, waiter_list, create_waiter, edit_waiter, delete_waiter, reception_list, create_reception, edit_reception, delete_reception, delete_order, edit_order

urlpatterns = [
    path('',home,name='home'),
    path('table/',table_list,name='table'),
    path('table/create/',create_table,name='create_table'),
    path('table/edit/<int:pk>/',edit_table,name='edit_table'),
    path('table/delete/<int:pk>/', delete_table, name='delete_table'),

    path('menu/',menu,name='menu'),
    path('menu/create/', create_menu, name='create_menu'),
    path('menu/edit/<int:pk>/',edit_menu,name='edit_menu'),
    path('menu/delete/<int:pk>/',delete_menu,name='delete_menu'),

    path('category/',category,name='category'),
    path('category/create/',create_category,name='create_category'),
    path('category/edit/<int:pk>/',edit_category,name='edit_category'),
    path('category/delete/<int:pk>/', delete_category, name='delete_category'),

    path('order/',order,name='order_list'),
    path('order/create/',create_order,name='create_order'),
    path('order/edit/<int:pk>/',edit_order,name='edit_order'),
    path('order/delete/<int:pk>/',delete_order,name='delete_order'),

    path('waiter/',waiter_list,name='waiter_list'),
    path('waiter/create/', create_waiter,name='create_waiter'),
    path('waiter/edit/<int:pk>',edit_waiter,name='edit_waiter'),
    path('delete/waiter/<int:pk>/',delete_waiter,name='delete_waiter'),

    path('reception/',reception_list,name='reception_list'),
    path('reception/create/',create_reception,name='create_reception'),
    path('reception/edit/<int:pk>',edit_reception,name='edit_reception'),
    path('reception/delete/<int:pk>',delete_reception,name='delete_reception'),
]