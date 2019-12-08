from django.urls import path
from . import views
from django.conf.urls import url
from .views import  RcLoginView, RcLogoutView, profile, ChangeUserInfoView, RcPasswordChangeView, RegisterDoneView
from .views import RegisterView, user_activate, DeleteUserView
from .captcha_decorators import check_recaptcha


urlpatterns = [
  path('login/', RcLoginView.as_view(), name = 'login'),
    path('register/',check_recaptcha(views.RegisterView.as_view()), name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('logout/', RcLogoutView.as_view(), name = 'logout'),
    path('profile-change/', ChangeUserInfoView.as_view(), name = 'profile_change'),
    path('profile-delete/', DeleteUserView.as_view(), name = 'profile_delete'),
    path('register_activate/<str:sign>/', user_activate, name = 'register_activate'),
    path('register_done/', RegisterDoneView.as_view(), name = 'register_done'),
    path('password-change/', RcPasswordChangeView.as_view(), name = 'password_change'),


]
