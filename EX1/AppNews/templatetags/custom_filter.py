from django import template

register = template.Library()
@register.filter()
def censor_rediska(text):
    censor_text = text.replace('Редиска', '****')
    return censor_text
