from django import forms
from django.contrib.auth import get_user_model, authenticate
from ..models import Author

User = get_user_model()

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        min_length=4,
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "myinput",
            "placeholder": "Enter your username"  
        })
    )
    password = forms.CharField(
        min_length=3,
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "myinput",
            "id": "password_field",
            "placeholder": "Enter password"
        })
    )
    class Meta:
        model = User
        fields = ("username", "password")
        

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")   

        user = authenticate(username=username, password=password)

        
        if not user:
            raise forms.ValidationError("username or password is wrong!")
        
        if not user.is_active or not user.is_staff:
            raise forms.ValidationError("Your account is deactivated")
        return self.cleaned_data
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({"class":"form-control"}) 

    