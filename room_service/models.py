from django.db import models
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.db.models import Sum, F, DecimalField


# Create your models here.
class RoomService(models.Model):
    PRD_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    content = models.CharField(max_length=30, default=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/', blank=True)

    CATEGORY_CHOICES = (
        # 값, 출력될 텍스트
        ('FNB', 'Food&Beverage'),
        ('BAS', 'Bath Amenity'),
        ('BED', 'Bedclothes'),
        ('ETC', 'Etc'),
    )
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES, default='FNB')    
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
   
    
    def __str__(self):
        return f"{self.PRD_name} {self.description} {self.price} {self.CATEGORY_CHOICES}"

class LangChoice(models.Model):
    LANG_CHOICES = [
        ('ko', 'Korean'),
        ('en', 'English'),
        ('ja', 'Japanese'),
        ('cn', 'Chinese'),
    ]

    language = models.CharField(
        max_length=2,
        choices=LANG_CHOICES,
        default='ko',
    )
    
    room_number = models.PositiveIntegerField()

class Product(models.Model):  # RoomService 모델을 Product로 변경
    PRD_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    content = models.CharField(max_length=30, default=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='midia/image/', blank=True)
    CATEGORY_CHOICES = (
        # 값, 출력될 텍스트
        ('FNB', 'Food&Beverage'),
        ('BAS', 'Bath Amenity'),
        ('BED', 'Bedclothes'),
        ('ETC', 'Etc'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='FNB')    

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
   
    def __str__(self):
        return f"{self.PRD_name} {self.description} {self.price} {self.CATEGORY_CHOICES}"

class Cart(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({"error": "Invalid product_id"}, status=400)
        product = Product.objects.get(id=product_id)
        cart_id = request.session.get('cart_id')
        if not cart_id:
            cart = Cart.objects.create(total=0)
            request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.get(id=cart_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        total_quantity = CartItem.objects.filter(cart=cart).aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_price = CartItem.objects.filter(cart=cart).aggregate(total_price=Sum(F('quantity') * F('product__price'), output_field=DecimalField()))['total_price']
        return JsonResponse({'total_quantity': total_quantity, 'total_price': str(total_price)})


