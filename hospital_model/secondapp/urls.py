from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('hospital/', views.index),
    path('hospital/<int:hospital_id>/',views.index2, name='index2'),
    path('hospital/hospital_table/', views.index3),
]
