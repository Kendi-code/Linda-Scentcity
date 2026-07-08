from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Secure, temporary migration endpoint
    path('execute-cloud-migration-v1/', views.run_production_migration, name='cloud_migration'),
]