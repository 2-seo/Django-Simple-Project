from django import forms
from .models import Myuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=65,
        label='사용자 이름',
        error_messages={
            'required': '아이디를 입력하세요.'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='비밀번호',
        error_messages={
            'required': '비밀번호를 입력하세요.'
        }
    )

    def clean(self):
        cleand_data = super().clean()
        username = cleand_data.get('username')
        password = cleand_data.get('password')

        if username and password:
            user = Myuser.objects.get(username=username)
            if not check_password(password, user.password):
                # password 가 일치하지 않으면 error 를 추가함
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                # 일치하면 user 객체에서 username 을 self.username 에 담음
                self.username = user.username