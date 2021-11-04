from django.template import Library

register = Library()

@register.filter
def tag_1(text):
    return f"{text[:5]}..."
