from django.shortcuts import render

# Create your views here.
def calculator(request):
    return render(request, 'calculator/index.html')

def result(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    print(request.META)
    context ={
        'message' : message,
        'message2' : message2,

    }
    return render(request, 'calculator/result.html', context)