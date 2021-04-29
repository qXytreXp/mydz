from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout')
]
