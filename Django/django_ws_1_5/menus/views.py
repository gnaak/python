from django.shortcuts import render

# Create your views here.

drink = ["cider","coke","miranda","fanta", "eye of finetree"]

def food(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    context = { 'food' : food,
    }
    return render(request, 'menus/food.html', context)

def receipt(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    message = request.GET.get('message')
    context ={
        'message' : message,
        'food' : food,
        'drink' : drink
    }
    return render(request, 'menus/receipt.html', context)

def drink(request):
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    context = { 'drink' : drink,
    }
    return render(request, 'menus/drink.html', context)

