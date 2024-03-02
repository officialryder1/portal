from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
   firstname = forms.CharField(max_length=200)

   class Meta:
        model = User
        fields = (
            'username', 'firstname', 'last_name', 'email', 'password1','password2'
        )
        help_texts = {
           k:"" for k in fields
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Comfirm Password'})
        }


          
