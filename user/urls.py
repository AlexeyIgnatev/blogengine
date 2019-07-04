from django.contrib.auth.views import LoginView
from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register_url'),
    path('profile/', ProfileView.as_view(), name='my_profile_url'),
    path('login/', LoginView.as_view(template_name='user/login.html', authentication_form=CustomAuthenticationForm),
         name='user_login_url'),
    path('logout/', LogoutView.as_view(), name='user_logout_url'),
    path('<str:username>/profile/', ProfileView.as_view(), name='other_profile_url'),
    path('profile/update/', ProfileEditView.as_view(), name='profile_edit_url')
]
