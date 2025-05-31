from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'forms-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'forms-control'}))
    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':'forms-control'}))
    password2 =  forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':'forms-control'}))
    
    class Meta:
        model = User
        fields=('username','email','password1','password2')
        
    
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        
        if p1 and p1 and p1 != p2:
            raise ValidationError("پسوورد ها مطابقت ندارد")

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'forms-control'}))
    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class':'forms-control'}))