from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        return render(request, 'shop/product_detail.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

# TEMPORARY MIGRATION TRIGGER VIEW
def run_production_migration(request):
    try:
        # This forces the live Supabase database to create your missing column
        call_command('migrate', interactive=False)
        return HttpResponse("<h1>Database Status: Migration Completed Successfully!</h1>")
    except Exception as error:
        return HttpResponse(f"<h1>Migration Interrupted</h1><p>Error details: {str(error)}</p>")