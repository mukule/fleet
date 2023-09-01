from django import template

register = template.Library()

@register.filter
def split_decimal(value):
    # Convert the decimal value to a string
    value_str = str(value)

    # Split the string into whole number and decimal parts
    parts = value_str.split('.')

    # If there's a decimal part, return both parts
    if len(parts) == 2:
        return parts[0], parts[1]

    # If there's no decimal part, return the whole number and an empty string for cents
    return parts[0], ""

