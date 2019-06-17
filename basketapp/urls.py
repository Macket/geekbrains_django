from django.urls import path

from .views import add, remove

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:product_pk>/', add, name='add'),
    path('remove/<int:product_pk>', remove, name='remove'),
]
