from django import template

register = template.Library()

@register.filter("has_group")
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
