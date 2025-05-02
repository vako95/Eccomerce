from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context.get('request')
    if request and request.resolver_match:
        return 'active' if request.resolver_match.url_name == url_name else ''
    return ''
