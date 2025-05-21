from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        min_length=8,
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "myinput",
            "id": "password_field",
            "placeholder": "Enter password"
        })
    )
    password_confirm = forms.CharField(
        min_length=8,
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            "class": "myinput",
            "id": "password_field",
            "placeholder": "Confirm your password"
        })
    )

    class Meta:
        model = User
        fields = ("username" , "email", "first_name", "last_name")

    def clean(self):
        cleaned_data = super().clean()     
        password = cleaned_data.get("password")    
        password_confirm = cleaned_data.get("password_confirm")
        
        if password and  len(password) < 8 :
            self.add_error("Password can't be short than 8")
        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Passwords do not match")
       

        return self.cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class":"form-control"})


