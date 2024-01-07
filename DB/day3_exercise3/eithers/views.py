from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentForm
from .models import Question, Comment
from random import randint
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)

def random(request):
    form = Question.objects.all()
    target = randint(1, len(form))
    return redirect('eithers:detail', target)

def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글의 모든 댓글을 조회(역참조)
    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'eithers/detail.html', context)

def comments_create(request, pk):
    # 게시글 조회 
    question = Question.objects.get(pk=pk)
    # CommentForm으로 사용자로부터 데이터를 입력 받음 
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment_form.save()
        return redirect('eithers:detail', question.pk)
    context = {
        'question':question,
        'comment_form':comment_form,
    }
    return render(request, 'eithers/detail.html', context)

