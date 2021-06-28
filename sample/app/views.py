from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('OK')
    # HTML 문자열로 작성
    # JSON로 작성
    # Template로 작성

def main(request):
    # return HttpResponse('<b><i>안녕하세요</i></b>')
    
    # return HttpResponse('''
    # <script>alert(1)</script>
    # <b><i>안녕하세요</i></b>
    # ''')
    
    # 카카오맵.html붙이기
    return render(request, 'kakao_map.html')
