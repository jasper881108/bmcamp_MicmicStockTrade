from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.forms import PasswordInput,ModelForm
from  .models import Account

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, help_text='Require. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email','username','password1','password2')


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
            # models.objects -> look into database,
            # get() -> get something,
            # filter() -> return query set of data
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
            # models.objects -> look into database,
            # get() -> get something,
            # filter() -> return query set of data
        except Exception as e:
            return username
        raise forms.ValidationError(f'username {username} is already in use.')
class AccountAuthenticationForm(ModelForm): #build form from scratch
    password = forms.CharField(label= 'password',widget=PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')
    def save(self,request):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email,password=password)
        if user:
            login(request,user)
    def clean(self):
    # default form doesn't know what it function as, here we define validation errors
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email,password=password):
                raise ValueError('這不是有效的帳號')

