from django import template

register=template.Library()
@register.filter('cut')


def cut(value,arg):
    """
    This cut out all values of 'args' from the string!
    :param values:
    :param arg:
    :return:
    """
    return value.replace(arg,'')
# register.filter('cut',cut)