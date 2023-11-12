from django.shortcuts import render, redirect
from .forms import UserBodyInputForm, UserCompareInputForm
from .models import UserBodyInput, UserCompareInput

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse  

@login_required
def user(request):
    # 사용자의 사이즈 정보가 있는지 확인
    try:
        user_body_input = request.user.userbodyinput
        # 기존 정보가 있는 경우, 수정을 위한 폼을 생성
        if request.method == 'POST':
            form = UserBodyInputForm(request.POST, instance=user_body_input)
            if form.is_valid():

                request.session['user_height'] = form.cleaned_data['height']
                request.session['user_weight'] = form.cleaned_data['weight']
                request.session['user_gender'] = form.cleaned_data['gender']

                form.save()
                messages.success(request, '사이즈 정보가 수정되었습니다.')
                return redirect('/user/compare')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserBodyInputForm(instance=user_body_input)
    except UserBodyInput.DoesNotExist:
        
        # 사용자의 사이즈 정보가 없는 경우, 새로운 정보를 입력하는 폼을 생성
        if request.method == 'POST':
            form = UserBodyInputForm(request.POST)
            if form.is_valid():
                
                user_body_input = form.save(commit=False)
                user_body_input.user = request.user
                user_body_input.save()
                messages.success(request, '사이즈 정보가 저장되었습니다.')
                return redirect('compare')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserBodyInputForm()
    
    return render(request, 'user/U_input.html', {'form': form})

def compare(request):

    print('user input34444', request.session['user_height'])

    # 사용자의 사이즈 정보가 있는지 확인
    try:
        # 기존 정보가 있는 경우, 수정을 위한 폼을 생성
        if request.method == 'POST':
            print('user 432432')

            form = UserCompareInputForm(request.POST)
            if form.is_valid():
                print('user 22222222')

                request.session['user_top'] = form.cleaned_data['top']
                request.session['user_bottom'] = form.cleaned_data['bottom']
                request.session['user_chest'] = form.cleaned_data['chest']
                request.session['user_shoulder'] = form.cleaned_data['shoulder']
                request.session['user_arm'] = form.cleaned_data['arm']
                request.session['user_neck'] = form.cleaned_data['neck']
                request.session['user_waist'] = form.cleaned_data['waist']
                request.session['user_ass'] = form.cleaned_data['ass']
                request.session['user_thighs'] = form.cleaned_data['thighs']

                #form.save()
                messages.success(request, '사이즈 정보가 수정되었습니다.')
                return redirect('/clothes')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserCompareInputForm()
    except UserBodyInput.DoesNotExist:
        # 사용자의 사이즈 정보가 없는 경우, 새로운 정보를 입력하는 폼을 생성
        if request.method == 'POST':
            form = UserBodyInputForm(request.POST)
            if form.is_valid():
                user_body_input = form.save(commit=False)
                user_body_input.user = request.user
                user_body_input.save()
                messages.success(request, '사이즈 정보가 저장되었습니다.')
                return redirect('')
            else:
                messages.error(request, '올바르지 않은 데이터가 포함되어 있습니다. 다시 시도해주세요.')
        else:
            form = UserBodyInputForm()
    
    return render(request, 'user/U_compare.html', {'form': form})