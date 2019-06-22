from django.urls import path

from .views import add, remove, basket, edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='read'),
    path('add/<int:product_pk>/', add, name='add'),
    path('remove/<int:product_pk>', remove, name='remove'),
    path('edit/<int:pk>/', edit, name='edit'),
]
