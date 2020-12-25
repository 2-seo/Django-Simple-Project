from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Myuser
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        # POST 일 경우 request 의 POST 데이터를 form 에 넣어줌
        form = LoginForm(request.POST)

        # form 에서 유효성 검사를 함 
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        # 아닐 경우에는 빈 폼 생
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Form 이용하기 전 method

# def login(request):
#
#     res_data = {}
#
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             if username and password:
#                 user = Myuser.objects.get(username=username)
#                 if check_password(password, user.password):
#                     # session
#                     request.session['user'] = user.username
#                     return redirect('/')
#                 else:
#                     res_data['error'] = '비밀번호를 확인하세요!'
#             else:
#                 res_data['error'] = '아이디와 패스워드를 입력하세요.'
#
#     return render(request, 'login.html', res_data)


def logout(request):
    # user 라는 session 이 있는지 Check
    if request.session['user']:
        # 있으면 delete
        del(request.session['user'])
    return redirect('/')

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
