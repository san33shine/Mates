from . import views
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ChangePasswordView


app_name='core'
urlpatterns = [
    path("", views.Index.as_view(), name = 'core_index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

]
