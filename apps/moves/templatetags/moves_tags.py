from django import template

register = template.Library()


@register.filter('add_class')
def add_class(field, valid=None):
    attrs = {'class': valid}
    return field.as_widget(attrs=attrs)
