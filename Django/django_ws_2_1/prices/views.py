from django.shortcuts import render

# Create your views here.
def price(request, name, num):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    items = list(product_price.keys())
    if name in items:
        price = product_price[name]*num,
    else:
        price = ''
    context = {
        'name': name,
        'num' : num,
        'price' : price,
        'items' : items,
    }
    return render(request, 'prices/price.html', context)