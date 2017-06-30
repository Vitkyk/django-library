from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def add_first(value, arg):
    return value + arg[0]


@register.filter
def add_last(value, arg):
    return value + arg[len(arg) - 1]


@register.filter
def subtract_first(value, arg):
    return value - arg[0]


@register.filter
def subtract_last(value, arg):
    return value - arg[len(arg) - 1]
