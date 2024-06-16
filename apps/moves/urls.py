from django.urls import path

from apps.moves.views import *

urlpatterns = [
    path('', MoveListView.as_view(), name='move-list'),
    path('create/', move_create, name='move-create'),
    path('update/<uuid:pk>/', MoveUpdateView.as_view(), name='move-update'),
    path('cancel/<uuid:pk>/', move_cancel, name='move-cancel'),

    path('str_product/create/<uuid:pk>', StrProductsCreateView.as_view(), name='str-product-create'),
    path('str_product/delete/<uuid:pk>', str_products_delete, name='str-product-delete')
]
