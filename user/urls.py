from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserRegisterView, UserLoginAPIView, SendVerificationCodeView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path('activation/', SendVerificationCodeView.as_view(), name='send-code'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
