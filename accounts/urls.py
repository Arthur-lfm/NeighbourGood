from django.urls import path
from . import views

# namespace for the app
app_name = "accounts"

# url patterns for the app
urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),
]