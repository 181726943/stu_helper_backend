import random
import string

from dj_rest_auth.views import PasswordResetView
from django.core.mail import EmailMessage
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework import status
from rest_framework.response import Response


class CustomPasswordResetView(PasswordResetView):
    def send_email(self, email, context):
        code = ''.join(random.choices(string.digits, k=6))
        subject = 'Password Reset'
        message = '重置密码验证码为: ' + code + "\n如非本人操作请忽略"
        emails = EmailMessage(subject, message, to=[email])
        emails.send()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


