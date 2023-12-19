from django.urls import path

from user.views import UserRegisterView, UserLoginAPIView, SendVerificationCodeView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path('activation/', SendVerificationCodeView.as_view(), name='send-code')
]
