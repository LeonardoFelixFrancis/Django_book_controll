from django import forms

class RegisterForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.widgets.PasswordInput)
    confirm_password = forms.CharField(widget=forms.widgets.PasswordInput)

class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput)