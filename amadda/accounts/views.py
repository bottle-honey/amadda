from django.contrib import auth
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse 
# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user_id=request.POST['username']
            user_password=request.POST['password1']
            user_email=request.POST['email']

            user = User(
                user_id = user_id,
                user_password = user_password,
                user_email = user_email
            )
            user.save()
            # auth.login(request, user)
            return render(request,'login.html')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

    # 로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST['username']
        user_password = request.POST['password']
        res_data = {}
        if not (user_id and user_password):
            res_data['error'] = '모든 칸을 다 입력하세요'
        else:
            # 기존 db에 있는 User 모델과 같은 값을 가져옴
            user = User.objects.get(user_id = user_id)
            if check_password(user_password, User.user_password):
                request.session['user_id'] = User.id
                render(request, 'logout.html')
            else:
                pass
    else:
        return render(request, 'login.html')
    return render(request, 'login.html', res_data)

# 로그아웃
def logout(request):
    if request.session['user_id']:
        del(request.session['user_id'])
    return redirect('/')

# home
def home(request):
    return render(request, 'home.html')