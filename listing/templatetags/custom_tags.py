import string
import re


from django import template

register = template.Library()


def cap_all_words(sentence):
    return string.capwords(sentence)

def fix_phone(phone):
    phone = re.sub("\D", "", phone)
    return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]

# {% load custom_tags %}
register.filter('cap_all_words', cap_all_words)
register.filter('fix_phone', fix_phone)