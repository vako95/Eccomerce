from django import template
import urllib.parse
register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context.get("request")
    if request and request.resolver_match:
        return "active" if request.resolver_match.url_name == url_name else ''
    return ""


@register.filter
def remove_page_num(query_string):
    parsed = urllib.parse.parse_qsl(query_string)
    cleaned = [(k, v) for k, v in parsed if k != 'page']
    return urllib.parse.urlencode(cleaned)


