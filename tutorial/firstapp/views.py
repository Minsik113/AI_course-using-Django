from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Curriculum

# Create your views here.
def main(request):
    return JsonResponse({'name': 'park',
                        'age': 37})

def insert(request):
    # 1-linus입력
    Curriculum.objects.create(name='linux')
    # 2- python입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js입력
    Curriculum(name='python').save()
    #4-django입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    # curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)
    
    # firstapp/templates/firstapp/show.html을 보여주자
    # return render(request, 'firstapp/show.html',{})

    curriculum = Curriculum.objects.all()
    return render(
        request, 'firstapp/show.html',
        {'data': curriculum}
    )

def template(request):
    curri = Curriculum.objects.all()
    data = {
        'curri': curri,
        'str': 'text', 'num': 10,
        'list': [1, 2, 3],
        'dict': {'a': 'aaa', 'b': 'bbb'}
    }
    return render(
        request, 'firstapp/template.html', data)

def index(request):
    return render( 
        request, 'index.html')
