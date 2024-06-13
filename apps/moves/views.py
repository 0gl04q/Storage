from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.moves.models import Movement


class MoveListView(ListView):
    model = Movement
    paginate_by = 5
    template_name = 'moves/move_list.html'
    extra_context = {'title': 'Список движений'}


class MoveDetailView(DetailView):
    model = Movement
    template_name = 'moves/move_detail.html'
    extra_context = {'title': 'Движение'}
