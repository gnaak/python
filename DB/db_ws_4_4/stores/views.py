from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm
# Create your views here.

def index(request):
    stores = Store.objects.all()
    context = {
        'stores':stores,
    }
    return render(request, 'stores/index.html', context)


def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_form = ProductForm()
    products = store.product_set.all()
    context = {
        'store':store,
        'product_form': product_form,
        'products': products,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            # article.user에 현재 로그인된 유저 저장 
            store.user = request.user
            form.save()
            return redirect('stores:index')
    else:
        form = StoreForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/create.html', context)

def delete(request, pk):
    store = Store.objects.get(pk=pk)
    if request.user == store.user:
        store.delete()
    return redirect('stores:index')

def product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_form = ProductForm(request.POST)
    if product_form.is_valid():
        product = product_form.save(commit=False)
        product.store = store
        product.user = request.user
        product_form.save()
        return redirect('stores:detail', store_pk)
    context = {
        'store': store,
        'product_form': product_form,
    }
    return render(request, 'stores/detail.html', context)


def comment_delete(request, store_pk, product_pk):
    product = Product.objects.get(pk=product_pk)
    product.delete()
    return redirect('stores:detail', store_pk)