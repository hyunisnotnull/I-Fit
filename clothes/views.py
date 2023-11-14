from django.shortcuts import render, redirect
from .forms import ClothingSizeInputForm
from django.contrib.auth.decorators import login_required

@login_required
def clothes(request):
    if request.method == 'POST':
        form = ClothingSizeInputForm(request.POST)
        

        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            print(f"thighs: {clothing_type}")

            clothing_type = form.cleaned_data['clothing_type']
            # 선택한 옷의 종류에 따라 필요한 옷 치수 입력을 요구하거나 입력된 데이터를 처리합니다.
            if clothing_type in ['outer', 'top']:
                # 상의 및 아우터의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                # 이어서 데이터 처리 코드를 작성
                # 데이터 저장 추가
            elif clothing_type in ['bottom', 'skirt']:
                # 바지 및 치마의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                waist = form.cleaned_data['waist']
                hip = form.cleaned_data['hip']
                bottom_length = form.cleaned_data['bottom_length']
                thigh = form.cleaned_data['thigh']
                # 이어서 데이터 처리 코드를 작성
            # 필요에 따라 딥러닝 모델로 데이터를 전달하고 추천 사이즈를 받는 코드를 작성
            # 세션에 입력된 옷 사이즈 데이터 저장
            request.session['clothing_type'] = clothing_type
            request.session['clothes_shoulder'] = shoulder
            request.session['clothes_chest'] = chest
            request.session['clothes_total_length'] = total_length
            request.session['clothes_sleeve'] = sleeve
            request.session['clothes_waist'] = waist
            request.session['clothes_hip'] = hip
            request.session['clothes_bottom_length'] = bottom_length
            request.session['clothes_thigh'] = thigh
            print(request.session)
            print("Form Data:", form.cleaned_data)

            return redirect('recommendation:recommendation')
    else:
        
        form = ClothingSizeInputForm()

    return render(request, 'clothes/C_input.html', {'form': form})
