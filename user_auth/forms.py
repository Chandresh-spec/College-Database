from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
       model=User
       fields=('username','email','password1','password2')



    

    def clean_email(self):
        email=self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exists")
        
        return email




class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('full_name','bio','phone','profile_img','city','gmail')

    

    




    

