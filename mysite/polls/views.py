from django.http.response import JsonResponse
from polls.models import Question
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm
from .forms import QuestionForm
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

# def question_create(request):
#     form = QuestionForm()
#     return render(
#         request, 'polls/question_form.html', 
#         {'form': form}
#     )
