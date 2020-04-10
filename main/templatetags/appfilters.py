from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='getheadline')
@stringfilter
def getheadline(string):
    spal=""
    if(len(string) > 180):
        spal=string[:180]
        spal = spal + "..."
        return spal
    else:
        return string

@register.filter(name='trimheadline')
@stringfilter
def trimheadline(string):
    spal=""
    if(len(string) > 75):
        spal=string[:75]
        spal = spal + "..."
        return spal
    else:
        return string

@register.filter(name='getvideotitle')
@stringfilter
def getvideotitle(string):
    spal=""
    if(len(string) > 60):
        spal=string[:60]
        spal = spal + "..."
        return spal
    else:
        return string

@register.filter(name='newssplit')
@stringfilter
def newssplit(string):
    spl = string.split('\n')
    return(spl)
