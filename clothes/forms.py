from django import forms

class ClothingSizeInputForm(forms.Form):
    CLOTHING_CHOICES = [
        ('outer', '아우터'),
        ('top', '상의'),
        ('bottom', '바지'),
        ('skirt', '치마'),
        ('long', '한벌옷'),
        ('shirt', '셔츠'),
    ]

    clothing_type = forms.ChoiceField(label='옷의 종류', choices=CLOTHING_CHOICES)
    
    # 모든 옷 치수 필드를 추가합니다. 초기에는 빈 필드로 시작합니다.
    shoulder = forms.FloatField(label='어깨너비 (cm)', required=False)
    chest = forms.FloatField(label='가슴단면 (cm)', required=False)
    total_length = forms.FloatField(label='총장 (cm)', required=False)
    sleeve = forms.FloatField(label='소매길이 (cm)', required=False)

    l_shoulder = forms.FloatField(label='어깨너비 (cm)', required=False)
    l_chest = forms.FloatField(label='가슴단면 (cm)', required=False)
    l_sleeve = forms.FloatField(label='소매길이 (cm)', required=False)

    s_shoulder = forms.FloatField(label='어깨너비 (cm)', required=False)
    s_chest = forms.FloatField(label='가슴단면 (cm)', required=False)
    s_total_length = forms.FloatField(label='총장 (cm)', required=False)
    s_sleeve = forms.FloatField(label='소매길이 (cm)', required=False)
    
    neck = forms.FloatField(label='목둘레 (cm)', required=False)
    ntk = forms.FloatField(label='총장 (cm)', required=False)

    waist = forms.FloatField(label='허리단면 (cm)', required=False)
    hip = forms.FloatField(label='엉덩이단면 (cm)', required=False)
    bottom_length = forms.FloatField(label='총장 (cm)', required=False)
    thighs = forms.FloatField(label='허벅지단면 (cm)', required=False)