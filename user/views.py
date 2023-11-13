from django.shortcuts import render, redirect
from .forms import UserBodyInputForm, UserCompareInputForm
from .models import UserBodyInput, UserCompareInput

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse  
import pandas as pd
from .utils import filter_data

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
                
                csv_file_path = 'data.csv'  
                model_data = pd.read_csv(csv_file_path)

                # 사용자 입력에서 필요한 값 추출
                user_height = request.session['user_height']
                user_weight = request.session['user_weight']
                user_gender = request.session['user_gender']

                # filter_data 함수 호출
                filtered_data = filter_data(model_data, user_height, user_weight, user_gender)


                average_top = filtered_data['top'].mean()
                average_chest = filtered_data['chest'].mean()
                average_shoulder = filtered_data['shoulder'].mean()
                average_arm = filtered_data['arm'].mean()
                average_neck = filtered_data['neck'].mean()
                average_ntk = filtered_data['ntk'].mean()
                average_waist = filtered_data['waist'].mean()
                average_ass = filtered_data['ass'].mean()
                average_bottom = filtered_data['bottom'].mean()
                average_thighs = filtered_data['thighs'].mean()
                
                request.session['average_top'] = average_top
                request.session['average_chest'] = average_chest
                request.session['average_shoulder'] = average_shoulder
                request.session['average_arm'] = average_arm
                request.session['average_neck'] = average_neck
                request.session['average_ntk'] = average_ntk
                request.session['average_waist'] = average_waist
                request.session['average_ass'] = average_ass
                request.session['average_bottom'] = average_bottom
                request.session['average_thighs'] = average_thighs

                
                print(f"top: {average_top}")
                print(f"chest: {average_chest}")
                print(f"shoulder: {average_shoulder}")
                print(f"arm: {average_arm}")
                print(f"neck: {average_neck}")
                print(f"ntk: {average_ntk}")
                print(f"waist: {average_neck}")
                print(f"ass: {average_ass}")
                print(f"bottom: {average_bottom}")
                print(f"thighs: {average_thighs}")

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
                average_top = request.session.get('average_top')
                average_chest = request.session.get('average_chest')
                average_shoulder = request.session.get('average_shoulder')
                average_arm = request.session.get('average_arm')
                average_neck = request.session.get('average_neck')
                average_ntk = request.session.get('average_ntk')
                average_waist = request.session.get('average_waist')
                average_ass = request.session.get('average_ass')
                average_bottom = request.session.get('average_bottom')
                average_thighs = request.session.get('average_thighs')

                user_top = form.cleaned_data['top']
                if user_top == 'big':
                    average_top *= 0.7
                elif user_top == 'small':
                    average_top *= 1.3
                user_bottom = form.cleaned_data['bottom']
                if user_bottom == 'big':
                    average_bottom *= 0.7
                elif user_bottom == 'small':
                    average_bottom *= 1.3
                user_chest = form.cleaned_data['chest']
                if user_chest == 'big':
                    average_chest *= 0.7
                elif user_chest == 'small':
                    average_chest *= 1.3
                user_shoulder = form.cleaned_data['shoulder']
                if user_shoulder == 'big':
                    average_shoulder *= 0.7
                elif user_shoulder == 'small':
                    average_shoulder *= 1.3
                user_arm = form.cleaned_data['arm']
                if user_arm == 'big':
                    average_arm *= 0.7
                elif user_arm == 'small':
                    average_arm *= 1.3
                user_neck = form.cleaned_data['neck']
                if user_neck == 'big':
                    average_neck *= 0.7
                elif user_neck == 'small':
                    average_neck *= 1.3
                user_waist = form.cleaned_data['waist']
                if user_waist == 'big':
                    average_waist *= 0.7
                elif user_waist == 'small':
                    average_waist *= 1.3
                user_ass = form.cleaned_data['ass']
                if user_ass == 'big':
                    average_top *= 0.7
                elif user_ass == 'small':
                    average_top *= 1.3
                user_thighs = form.cleaned_data['thighs']
                if user_thighs == 'big':
                    average_thighs *= 0.7
                elif user_thighs == 'small':
                    average_thighs *= 1.3

                request.session['predict_top'] = average_top
                request.session['predict_chest'] = average_chest
                request.session['predict_shoulder'] = average_shoulder
                request.session['predict_arm'] = average_arm
                request.session['predict_neck'] = average_neck
                request.session['predict_ntk'] = average_ntk
                request.session['predict_waist'] = average_waist
                request.session['predict_ass'] = average_ass
                request.session['predict_bottom'] = average_bottom
                request.session['predict_thighs'] = average_thighs
                
                # 정상적으로 사용자 신체 치수 예측 확인용 문구 추후 삭제 예정
                print(f"top: {average_top}")
                print(f"chest: {average_chest}")
                print(f"shoulder: {average_shoulder}")
                print(f"arm: {average_arm}")
                print(f"neck: {average_neck}")
                print(f"waist: {average_waist}")
                print(f"ass: {average_ass}")
                print(f"bottom: {average_bottom}")
                print(f"thighs: {average_thighs}")

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