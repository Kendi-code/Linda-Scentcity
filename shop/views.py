from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core.management import call_command

def run_production_migration(request):
    """
    A temporary utility view to programmatically execute model migrations
    against the cloud PostgreSQL production database engine.
    """
    try:
        # Programmatically trigger the equivalent of 'python manage.py migrate'
        call_command('migrate', interactive=False)
        return HttpResponse("<h1>Database Status: Migration Completed Successfully!</h1>")
    except Exception as error:
        return HttpResponse(f"<h1>Migration Interrupted</h1><p>Error details: {str(error)}</p>")

def home(request):
    # TEMPORARY BYPASS: Commeted out to stop the database crash loop
    # products = Product.objects.all()
    # return render(request, 'shop/index.html', {'products': products})
    
    return HttpResponse("<h1>Linda Scentcity Hub: Online</h1><p>Please go to your URL bar and add <strong>/execute-cloud-migration-v1/</strong> to the end of your link to repair the database.</p>")

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required(login_url='login')
def custom_dashboard(request):
    # TEMPORARY BYPASS: Commented out to prevent dashboard crash during setup
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('custom_dashboard')
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'shop/dashboard.html', {'form': form, 'products': products})
    """
    return HttpResponse("Dashboard locked during database migration setup.")

@login_required(login_url='login')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('custom_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})

@login_required(login_url='login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # We only delete if it's a POST request for security
    if request.method == 'POST':
        product.delete()
        
    return redirect('custom_dashboard')