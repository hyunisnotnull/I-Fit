from django import forms
from .models import UserBodyInput, UserCompareInput

class UserBodyInputForm(forms.ModelForm):
    class Meta:
        model = UserBodyInput
        fields = ['height', 'weight', 'gender']


class UserCompareInputForm(forms.ModelForm):
    class Meta:
        model = UserCompareInput
        fields = ['top', 'bottom', 'chest', 'shoulder', 'arm', 'neck', 'waist', 'ass', 'thighs']