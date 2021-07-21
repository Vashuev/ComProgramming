from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)[0]

@register.filter
def get_status(dictionary, key):
    return dictionary.get(key)[1]

@register.filter
def is_done(dictionary, key):
    if key:
        return 'completed'
    else:
        return 'incomplete'

@register.filter
def is_removing(dictionary, key):
    return dictionary.get('remove')

@register.filter
def is_adding(dictionary, key):
    return dictionary.get('add')
