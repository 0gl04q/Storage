from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from apps.moves.models import Movement, StrProduct
from apps.moves.forms import MoveForm, StrProductForm


class MoveListView(ListView):
    queryset = Movement.active.all()
    paginate_by = 5
    template_name = 'moves/move_list.html'
    extra_context = {'title': 'Список движений',
                     'buttons': {'Создать': reverse_lazy('move-create')}}


def move_create(request):
    move = Movement.objects.create(user=request.user)
    return redirect(to=reverse('move-update', args=(move.id,)))


def move_cancel(request, pk):
    move = Movement.objects.filter(pk=pk)
    move.update(is_active=False)
    return redirect(to=reverse('move-list'))


class MoveUpdateView(UpdateView):
    model = Movement
    form_class = MoveForm
    template_name = 'moves/move_create.html'
    extra_context = {'title': 'Изменение движения',
                     'button_save': True}
    success_url = reverse_lazy('move-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['str_products'] = StrProduct.objects.filter(move=self.object)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StrProductsCreateView(CreateView):
    model = StrProduct
    form_class = StrProductForm
    template_name = 'moves/str_product_create.html'
    extra_context = {'title': 'Добавление продукта',
                     'button_save': True}

    def get_success_url(self):
        move_id = self.kwargs.get('pk')
        return reverse_lazy('move-update', kwargs={'pk': move_id})

    def form_valid(self, form):
        move = Movement.objects.get(pk=self.kwargs.get('pk'))
        form.instance.move = move
        return super().form_valid(form)


def str_products_delete(request, pk):
    str_product = StrProduct.objects.get(pk=pk)
    move = str_product.move
    str_product.delete()
    return redirect(to='move-update', pk=move.pk)
