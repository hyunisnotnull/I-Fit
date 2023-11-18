from django.shortcuts import render, redirect
from .forms import ClothingSizeInputForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def clothes(request):
    if request.method == 'POST':
        form = ClothingSizeInputForm(request.POST)

        print('insert clothes')
        print( request.session.get('user_height') )

        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            clothing_type = form.cleaned_data['clothing_type']
            request.session['clothing_type'] = clothing_type
            # 선택한 옷의 종류에 따라 필요한 옷 치수 입력을 요구하거나 입력된 데이터를 처리합니다.
            if clothing_type in ['outer', 'top']:
                # 상의 및 아우터의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                # 데이터 저장 추가
                request.session['shoulder'] = shoulder
                request.session['chest'] = chest * 2
                request.session['total_length'] = total_length
                request.session['sleeve'] = sleeve

            elif clothing_type in ['bottom', 'skirt']:
                # 바지 및 치마의 치수 입력 필드가 비어 있지 않다면, 해당 데이터를 처리
                waist = form.cleaned_data['waist'] 
                hip = form.cleaned_data['hip']
                bottom_length = form.cleaned_data['bottom_length']
                thigh = form.cleaned_data['thigh']

                request.session['waist'] = waist * 2
                request.session['hip'] = hip * 2
                request.session['bottom_length'] = bottom_length
                request.session['thigh'] = thigh * 2
                
            elif clothing_type in ['long']:
                
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                
                request.session['shoulder'] = shoulder
                request.session['chest'] = chest * 2
                request.session['total_length'] = total_length
                request.session['sleeve'] = sleeve


            elif clothing_type in ['shirt']:
                shoulder = form.cleaned_data['shoulder']
                chest = form.cleaned_data['chest']
                total_length = form.cleaned_data['total_length']
                sleeve = form.cleaned_data['sleeve']
                neck = form.cleaned_data['neck']
                
                request.session['shoulder'] = shoulder
                request.session['chest'] = chest * 2
                request.session['total_length'] = total_length
                request.session['sleeve'] = sleeve
                request.session['neck'] = neck

            print(form.cleaned_data)
            return redirect('/recommendation')
        print(f"Session data after recommend_size: {request.session}")
    else:

        form = ClothingSizeInputForm()
    return render(request, 'clothes/C_input.html', {'form': form})
