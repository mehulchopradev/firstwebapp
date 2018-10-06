from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'library'

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.showlogin, name='login-page'),
    path('reg/', views.showregister, name='register-page'),
    path('users/', views.registeruser, name='register-user'),
    path('auth/', views.authenticateuser, name='auth-user'),
    path('home/', views.showhome, name='home-page'),
    path('books/<int:bookId>', views.showbook, name='show-book'),
    path('logout/', views.logout, name='logout'),
    path('issue-book/<int:bookId>', views.issuebook, name='issuebook'),
    path('return-book/<int:bookId>', views.returnbook, name='returnbook')
]
