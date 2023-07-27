from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_cart_total(context):
    cart = context['request'].session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return total_price

@register.simple_tag
def get_cart_quantity(cart_items):
    return sum(item_info['quantity'] for item_info in cart_items)
