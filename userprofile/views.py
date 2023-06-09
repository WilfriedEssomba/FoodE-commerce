from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import Userprofile
from store.forms import ProductForm
from store.models import Product, Order, OrderItem

# Create your views here.
def resto_details(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'resto_detail.html',{'user': user})
@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user)

    return render(request, 'my_store.html', {
        'products': products,
        'order_items': order_items
    })
@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'my_store_order_detail.html', {
        'order': order
    })


@login_required
def edit_product(request, pk):
    products = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=products)

        if form.is_valid():
            form.save()

            messages.success(request, 'Changes saved successfully')


            return redirect('my_store')
    else:
        form = ProductForm(instance=products)
    
    return render(request, 'add_product.html', {'form': form,'title': 'Edit Product'})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'Product added successfully')

            return redirect('my_store')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form, 'title': 'Add Product'})

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'The product was deleted!')

    return redirect('my_store')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html',{'form': form})
