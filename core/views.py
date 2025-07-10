from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Product,Category
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})

def products(request):
    q = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()

    if q:
        products = products.filter(name__icontains=q)
    
    if category_id:
        products = products.filter(category__id=category_id)

    paginator = Paginator(products, 8)  # 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'core/products.html', {
        'products': page_obj,
        'categories': categories,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Related products from same category
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]

    return render(request, 'core/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.send_email()
        success = True
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'success': success
    })
