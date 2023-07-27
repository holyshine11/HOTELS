from room_service.models import RoomService, LangChoice
from django.views.generic import TemplateView, ListView, FormView, DetailView, CreateView
from .forms import LangChoiceForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import RoomService
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from .models import Product, Cart, CartItem
from django.views.decorators.http import require_POST


class HomeView(TemplateView):
    template_name = 'room_service/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'Smart Room Service'
        return context


class LangView(FormView):
    template_name = 'room_service/lang.html'
    form_class = LangChoiceForm
    success_url = reverse_lazy('room_service:home')  # URL 패턴 이름을 참조

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    

class BathListView(ListView):
    model = RoomService
    queryset = RoomService.objects.order_by('PRD_name', 'description', 'price', 'image')
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'Bath Amenity Service'
        return context


class CategoryListView(ListView):
    model = RoomService
    context_object_name = 'room'

    def get_queryset(self):
        # 카테고리 값을 URL에서 추출합니다.
        category = self.kwargs['category']

        # 추출된 카테고리에 해당하는 상품만 필터링합니다.
        return RoomService.objects.filter(category=category).order_by('PRD_name', 'description', 'price', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        category_names = {
            'FNB': 'Food&Beverage',
            'BAS': 'Bath Amenity Service',
            'BED': 'Bedclothes Service',
            'ETC': 'ETC Service',
        }
        context['navbar_title'] = category_names.get(category, 'Service')
        return context

    def get_template_names(self):
        # 카테고리 값을 URL에서 추출합니다.
        category = self.kwargs['category']
        
        # 템플릿 파일의 경로를 지정합니다.
        template_name = f'room_service/{category}.html'
        return [template_name]

class FoodDetailView(DetailView):
    model = RoomService
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'Food&Beverage'
        return context

    def get_template_names(self):
        return ['room_service/FNB_detail.html']


class BathDetailView(DetailView):
    model = RoomService
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'Bath Amenity Service'
        return context
    
    def get_template_names(self):
        return ['room_service/BAS_detail.html']


class BedDetailView(DetailView):
    model = RoomService
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'Bedclothes Service'
        return context

    def get_template_names(self):
        return ['room_service/BED_detail.html']


class ETCDetailView(DetailView):
    model = RoomService
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_title'] = 'ETC Service'
        return context

    def get_template_names(self):
        return ['room_service/ETC_detail.html']


# 장바구니 
class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = RoomService.objects.get(id=product_id)
        cart = request.session.get('cart', {})
        
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {'quantity': 1, 'id': product.id, 'name': product.PRD_name, 'price': product.price}
            
        request.session['cart'] = cart
        return JsonResponse({'message': '상품이 장바구니에 추가되었습니다.', 'product_name': product.PRD_name})

    

class CartView(TemplateView):
    template_name = 'room_service/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        print("Cart Info:", cart)  # 디버깅을 위해 카트 정보 출력
        cart_items = []
        for product_id, item_info in cart.items():
            item = RoomService.objects.filter(id=product_id).first()  # 'id' 키 대신 'product_id' 변수 사용
            if item:  # 해당 아이템이 존재하면
                item_info['item'] = item
                cart_items.append(item_info)
        context['cart_items'] = cart_items
        context['navbar_title'] = "Cart"  # navbar title
        return context



# 장바구니 수량 카운트 뷰
class ModifyCartView(View):
    http_method_names = ['post']

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, product_id, *args, **kwargs):  
        quantity = int(request.POST.get('quantity'))  # string 값을 int로 변환

        try:
            product = RoomService.objects.get(id=product_id)  # RoomService로 변경
        except RoomService.DoesNotExist:  # RoomService로 변경
            return JsonResponse({'error': 'Product does not exist'}, status=400)  

        # 장바구니에서 상품의 수량을 업데이트
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] = quantity
            request.session['cart'] = cart
        else:
            return JsonResponse({'error': 'Product not in cart'}, status=400)

        # 업데이트된 총 수량과 총 가격을 계산
        total_quantity = sum(item['quantity'] for item in cart.values())
        total_price = sum(RoomService.objects.get(id=int(product_id)).price * item['quantity'] for product_id, item in cart.items())  # RoomService로 변경

        return JsonResponse({'total_quantity': total_quantity, 'total_price': total_price})



class CheckoutView(TemplateView):
    template_name = 'room_service/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        cart_items = []
        total_price = 0

        for product_id, item_info in cart.items():
            item = RoomService.objects.get(id=product_id)
            item_info['item'] = item
            total_price += item.price * item_info['quantity']
            cart_items.append(item_info)
        
        context['cart_items'] = cart_items
        context['total_price'] = total_price
        return context


# views.py
class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})
        
        if product_id in cart:
            del cart[product_id]
            
        request.session['cart'] = cart
        return redirect('room_service:cart')



def remove_from_cart(request, item_id):
    return redirect('room_service:cart')# 장바구니 페이지로 다시 리다이렉트


class DeleteSelectedView(View):
    def post(self, request, *args, **kwargs):
        selected_items = request.POST.getlist('selected_items')  # 사용자가 선택한 상품들의 id 리스트를 가져옴
        RoomService.objects.filter(id__in=selected_items).delete()  # 선택한 상품들을 삭제함
        return redirect('room_service:home')  

class DeleteSelectedItemsView(View):
    def post(self, request, *args, **kwargs):
        selected_items = request.POST.getlist('selected_items')
        for item_id in selected_items:
            if item_id in request.session.get('cart', {}):
                del request.session['cart'][item_id]
                request.session.modified = True
        return redirect('room_service:cart')
    
