from django import urls
from django.urls import path
from . import views

urlpatterns  = [
    path('', views.index, name='index'),
    path('<int:product_id>/detail', views.detail, name='detail'),
    path('category/<int:category_id>', views.get_products_by_category, name='category'),
    path('comment/<int:product_id>', views.comment_view, name='create_comment'),
]