from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from secondapp.models import Hospital

# Create your views here.
def index(request):
    hospital_list = Hospital.objects.order_by('id')
    print(hospital_list)
    return render(
        request, 'secondapp/home.html',
        {'hospital_list':hospital_list}
    )

def index2(request, hospital_id):
    hospital_list2 = get_object_or_404(Hospital, id=hospital_id)
    return render(
        request, 'secondapp/home2.html',
        {'hospital_list2':hospital_list2}
    )

def index3(request):
    hospital_list3 = Hospital.objects.all()
    return render(
        request, 'secondapp/home3.html',
        {'hospital_list3':hospital_list3}
    )