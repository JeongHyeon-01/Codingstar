from django.urls import path
from . import views
import user.views
from .views import Signin, Signup, logout,UpdateProfile

app_name = 'user'

urlpatterns = [
    path('', Signin.as_view(), name='signin'),
    path('signup', Signup.as_view(), name='signup'),
    path("logout", views.logout, name="logout"),
    path('profile/upload', UpdateProfile.as_view(), name='profile_update'),
]
