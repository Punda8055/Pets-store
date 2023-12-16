from django.urls import path
from . import views

urlpatterns = [
    path('pets',views.list_pets,name='list_pets'),
    path('/<int:id>',views.pet_detail,name='pet_detail'),   #/<int:id>
    path('',views.register,name='user_register'),
    path('login',views.user_login,name='user_login'),
    path('profile',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='user_logout'),
    path('search/',views.search_results, name='search_results'),


    # path('home', views.home, name='home'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pet_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:pet_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
]