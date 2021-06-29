from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create,
        name='answer_create'),
    path('question/create/', views.question_create,
        name='question_create'),
    path('signup/', views.signup, name='signup'),

]