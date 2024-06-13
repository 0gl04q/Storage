from django.urls import path

from apps.moves.views import *

urlpatterns = [
    path('', MoveListView.as_view(), name='move-list'),
    path('<uuid:pk>/', MoveDetailView.as_view(), name='move-detail')
]
