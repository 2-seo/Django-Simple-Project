from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from .models import Myuser


def register(request):
    # mapping 한 url 로 사용자가 들어오면 GET 방식으로 들어오게 됨
    # 사용자가 들어오면 register.html 을 render 해줌
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # request 에서 응답을 받을 때 dictionary 로 값을 전달 받는데,
        # .get 메서드를 통해서 key 가 있는지를 확인하고
        # 없으면 기본값으로 None 으로 설정함
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        if password != re_password:
            res_data['error'] = '비밀번호를 확인하세요.'
        else:
            user = Myuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            user.save()

        return render(request, 'register.html', res_data)
