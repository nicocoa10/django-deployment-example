# create filters here , ea custom tags

from django import template

register = template.Library()


# write a function that is gonna be your custom filter\

#Using decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all values of arg from the string
    """

    return value.replace(arg,'')

# register.filter('cut', cut) #you pass the name your gonna use to call the function from tag , and then pass the function you implemented
