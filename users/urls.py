from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_form, name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_form, name="register_user"),
]
