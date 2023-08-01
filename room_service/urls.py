from django.urls import path
from .views import HomeView, BathListView, CategoryListView, FoodDetailView, BathDetailView, BedDetailView, ETCDetailView, CartView, AddToCartView, DeleteSelectedView, DeleteSelectedItemsView
from . import views

app_name = 'room_service'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lang/', views.LangView.as_view(), name='lang'),
    path('room/', BathListView.as_view(), name='room'),
    path('room/<str:category>/', CategoryListView.as_view(), name='category-room'),
    path('room/FNB/<int:pk>/', FoodDetailView.as_view(), name='FNB'),
    path('room/BAS/<int:pk>/', BathDetailView.as_view(), name='BAS'),
    path('room/BED/<int:pk>/', BedDetailView.as_view(), name='BED'),
    path('room/ETC/<int:pk>/', ETCDetailView.as_view(), name='ETC'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('modify_cart/<int:product_id>/', views.ModifyCartView.as_view(), name='modify_cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_cart/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('delete_selected/', DeleteSelectedView.as_view(), name='delete_selected'),
    path('cart/delete_selected_items/', DeleteSelectedItemsView.as_view(), name='delete_selected_items'),
    path('delete_selected_items/', DeleteSelectedItemsView.as_view(), name='delete_selected_items'),
]