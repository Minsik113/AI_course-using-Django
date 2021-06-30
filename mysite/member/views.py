from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Member
from django.utils import timezone

# Create your views here.
def join(request):
    if request.method == 'GET':
        return render(request, 'member/join.html')
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']

        m = Member(
            user_id = user_id, user_pw=user_pw,
            user_name = user_name)
        m.c_date = timezone.now()
        m.save()

        return HttpResponse('가입 완료' + user_id + user_pw + user_name)

def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        try:
            member = \
                Member.objects.get(user_id=user_id, user_pw=user_pw)
        except:            
            return HttpResponse('로그인 실패')
        else:
            # 세션에 로그인 관련 정보 저장
            request.session['user_id'] = user_id
            
            a = request.session['user_id']
            # del request.session['user_id'] 로그아웃

            return HttpResponse('로그인 성공')

def logout(request):
    del request.session['user_id']
    return redirect('/login/') # 실제경로 혹은 url에 쓰여있는 이름

import glob
def upload1(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('my_file')
        # 6월1일(화)일정안내.pptx
        # 6월1일(화)일정안내_13148197.pptx
        name = upload_file.name
        size = upload_file.size

        f_list = glob.glob('*') # 모든파일명시
        print(f_list)
        if name in f_list: # 파일이 존재한다면
            print('존재하고 있음')

        # with open(name, 'wb') as file: # 저장이 전체 directory에 됨.
        with open('static/%s' % name, 'wb') as file: # static폴더에 저장 됨
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'upload1.html', {})

import os
from config import settings
def download(request):
    # filepath = os.path.join(settings.BASE_DIR, '경로/파일명')
    # c:/dev/django/mysite/db.sqlite3 
    filepath = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    filename = filepath.split('/')[-1]
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response