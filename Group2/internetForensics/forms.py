
"""from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    username = forms.charField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('passwrod')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid Password or Username')

