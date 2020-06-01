from django import template

regist = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Short summary.

    Parameters
    ----------
    value : type
        Description of parameter `value`.
    arg : type
        Description of parameter `arg`.

    Returns
    -------
    type
        This cuts out all values of "arg" from the string

    """
    return value.replace(arg, '')
