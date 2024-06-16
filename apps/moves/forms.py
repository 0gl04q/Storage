from django import forms

from apps.moves.models import Movement, StrProduct


class MoveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = list(self.fields)

        for field in fields:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})

    class Meta:
        model = Movement
        exclude = ('is_active', 'user')


class StrProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = list(self.fields)

        for field in fields:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})

    class Meta:
        model = StrProduct
        fields = ('product', 'purchase_price', 'quantity')
