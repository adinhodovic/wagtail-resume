from django import template

register = template.Library()


@register.filter
def space_to_plus(value):
    return value.replace(" ", "+")


@register.filter
def get_fields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]
