from polls.models import Question
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm
from django.contrib.auth import authenticate, login
from .forms import UserForm

from django.contrib.auth.models import User
def check(request):
    name = request.GET.get('username')
    # u = User.obejcts.get(username=name)
    # return JsonResponse({'result:': 'u.username'})
    try:
        u = User.objects.get(username=name)
        result = False
    except:
        result = True
    return JsonResponse({'result': result})

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(
        request, 'polls/question_list.html',
        {'question_list': question_list}
    )

    # result = [q.subject for q in question_list ]
    # return JsonResponse(result, safe=False)
    # return HttpResponse(str(result))

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    return render(
        request, 'polls/question_detail.html',
        {'question':question}
    )

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(
        content=request.POST.get('content'), 
        create_date=timezone.now())
    
    # aa = request.POST.get('aa') # name=='aa'인 값을 post로 넘겼으니 여기서 쓸 수 있다?
    # return HttpResponse(aa)
    return redirect('polls:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('polls:index')
    else:
        form = QuestionForm()
        
    context = {'form': form}
    return render(request, 'polls/question_form.html', context)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('polls:index') # redirect의 url의 name으로 접근하는방법이 이렇게 됨.
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

