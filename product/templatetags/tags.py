import datetime
from django import template

register = template.Library()

# Создание фильтра
@register.filter()
def my_media(vol):
    if vol:
        # return f'/media/{vol}'
        return f'{vol}'


    return '#'

