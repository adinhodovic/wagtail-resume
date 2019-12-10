from django import template

register = template.Library()


@register.filter
def space_to_plus(value):
    return value.replace(" ", "+")
