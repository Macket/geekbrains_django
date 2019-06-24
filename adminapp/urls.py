from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # url(r'^users/create/$', adminapp.user_create, name='user_create'),
    # url(r'^users/read/$', adminapp.users, name='users'),
    # url(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    # url(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    # url(r'^categories/create/$', adminapp.category_create,name='category_create'),
    # url(r'^categories/read/$', adminapp.categories, name='categories'),
    # url(r'^categories/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    # url(r'^categories/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]
