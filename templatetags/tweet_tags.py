import requests
from django import template

register = template.Library()

@register.simple_tag
def tweet_tags(url):
    twtjson = requests.get('https://publish.twitter.com/oembed?url=' + url + '&omit_script=true')
    twtparse = twtjson.json()
    twthtml = twtparse['html']
    return twthtml
