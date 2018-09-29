from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('login/', views.showlogin, name='login-page'),
    path('reg/', views.showregister, name='register-page')
]
