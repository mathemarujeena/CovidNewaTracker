from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "users"   


urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]