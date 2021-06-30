from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from polls import views
from member import views as m_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('join/', m_views.join),
    path('login/', m_views.login),
    path('logout/', m_views.logout),

    path('upload1/', m_views.upload1),
    path('download/', m_views.download),

    path('polls/', include('polls.urls')),
    path('login/', auth_views.LoginView.as_view(
            template_name = 'login.html'),
        name ='login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
]
