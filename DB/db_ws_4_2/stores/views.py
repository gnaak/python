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


def detail(request, pk):
    store = Store.objects.get(pk=pk)
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
            return redirect('stores:detail', store.pk)
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