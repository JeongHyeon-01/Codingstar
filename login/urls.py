from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

appname = 'login'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="login/login.html"), name='signin'),
    path('signup/', views.signup, name='signup'),
    path('anthorlogin/', views.anotherlogin, name='anotherlogin')
]