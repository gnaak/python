from django.shortcuts import render

# Create your views here.
def first(request):
    message3 = request.GET.get('message3')
    context ={
        'message3' : message3,
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    message1 = request.GET.get('message1')
    context ={
        'message1' : message1,
    }
    return render(request, 'throw_loops/second.html', context)


def third(request):
    message2 = request.GET.get('message2')
    message4 = request.GET.get('message4')
    context ={
        'message2' : message2,
        'message4' : message4,
    }
    return render(request, 'throw_loops/third.html', context)

