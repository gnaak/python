# views.py

from django.shortcuts import render

def index(request):
    # fruits = []
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]
    # for fruit in fruit_list:
    #     if fruit not in hate and len(fruit) >=2:
    #         fruits.append(fruit[:3])

    context ={'fruit_list':fruit_list, 'hate':hate}

    return render(request, 'fruits/index.html', context)

