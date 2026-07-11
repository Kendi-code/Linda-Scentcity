from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    path('dashboard/', views.custom_dashboard, name='custom_dashboard'),
    path('dashboard/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('dashboard/delete/<int:product_id>/', views.delete_product, name='delete_product'),
]