from django import forms
from django.forms import ModelForm
from app.models import employee
from  django.db.models import fields
from django.contrib.auth import authenticate, get_user_model, login, logout

class userLogin(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required = True,)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required = True,)

    class Meta():
        model = employee
        fields = ['username', 'password']


class userRegister(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),required = True,max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),required = True,max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required = True,max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required = True,max_length=50)
    
    class Meta():
        model = employee
        fields = ['name','email','username','password']


# def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         # user = authenticate(username = username,password=password)
#         user_name = employee.objects.filter(username = username)
#         if user_name.count() == 1:
#             user_object = employee.objects.get(username = username)
#             if user_object.username == username and user_object.password == password:
#                 raise forms.ValidationError("The user exists")
#         # if username and password:
#         #     if not user:
#         #         raise forms.ValidationError("The user does not exist")
#         #     if not user.check_password(password):
#         #         raise forms.ValidationError("Incorrect password")
#         #     if not user.is_active:
#         #         raise forms.ValidationError("the user is no longer active")

#         return super(userLogin,self).clean(*args, **kwargs)
    
#     # class Meta():
#     #     model = employee
#     #     fields = ['username','password']