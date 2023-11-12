from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth import login
import hashlib

# Create your views here.

# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            response = redirect('/')
            response.set_cookie('username', hashlib.sha256(user.username.encode()).hexdigest()) # 쿠키 설정
            return response
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'accounts/signup.html')

# 로그인
def login(request):
    context = {}  # context 딕셔너리 생성
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            print(request.user.is_authenticated)  # 로그인 후에는 True가 출력되어야 합니다.
            response = redirect('/')
            response.set_cookie('username', hashlib.sha256(user.username.encode()).hexdigest()) # 쿠키 설정
            return response
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            context['error'] = '아이디나 비밀번호가 잘못되었습니다.'
            return render(request, 'accounts/login.html', context)
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'accounts/login.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        print(request.user.is_authenticated)  # 로그아웃 전에는 True가 출력되어야 합니다.
        auth.logout(request)
        print(request.user.is_authenticated)  # 로그아웃 후에는 False가 출력되어야 합니다.
        request.session.flush()  # 세션 정보 삭제
        response = redirect('main:main')
        response.delete_cookie('username') # 쿠키 삭제
        response['Cache-Control'] = 'no-store' # 캐시 방지
        return response

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'accounts/login.html')
