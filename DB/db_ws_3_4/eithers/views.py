from django.shortcuts import render, redirect, get_object_or_404

from .models import Question, Comment
from .forms import QuestionForm, CommentForm

def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:index')
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    R_cnt = B_cnt = 0
    for comment in comments:
        if comment.pick:
            B_cnt +=1
        else:
            R_cnt +=1 
    B_pro = B_cnt/(R_cnt+B_cnt)*100
    R_pro = R_cnt/(R_cnt+B_cnt)*100
    context = {
        'question': question,
        'comment_form': comment_form,
        'B_cnt': B_cnt,
        'R_cnt': R_cnt,
        'B_pro': B_pro,
        'R_pro': R_pro
    }
    return render(request, 'eithers/detail.html', context)


def random(request):
    import random

    pk_list = []
    for value in Question.objects.values('pk'):
        pk_list.append(value['pk'])
    random_pk=random.choice(pk_list)
    
    return redirect('eithers:detail', random_pk)


def comment_create(request, question_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.question_id = question_pk
            comment.save()
    return redirect('eithers:detail', question_pk)

def update(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid:
            form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm(instance=question)
    context = {
        'question' : question,
        'form' : form,
    }
    return render(request, 'eithers/update.html', context)

def delete(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    return redirect('eithers:index')


def comment_delete(request, question_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('eithers:detail', question_pk)