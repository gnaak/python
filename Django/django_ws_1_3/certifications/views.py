from django.shortcuts import render
import random

# Create your views here.
def certifications1(request):
    age = [i for i in range(25,31)]
    grade = ['S','A','B','C']
    age_rd = random.choice(age)
    grade_rd = random.choice(grade)

    context = {
        'age_rd' : age_rd,
        'grade_rd' : grade_rd
    }

    return render(request, 'certifications/certifications1.html', context)

def certifications2(request):
    age = [i for i in range(25,31)]
    grade = ['S','A','B','C']
    age_rd = random.choice(age)
    grade_rd = random.choice(grade)

    context = {
        'age_rd' : age_rd,
        'grade_rd' : grade_rd
    }

    return render(request, 'certifications/certifications2.html', context)

def certifications3(request):
    age = [i for i in range(25,31)]
    grade = ['S','A','B','C']
    age_rd = random.choice(age)
    grade_rd = random.choice(grade)

    context = {
        'age_rd' : age_rd,
        'grade_rd' : grade_rd
    }

    return render(request, 'certifications/certifications3.html', context)