from django import forms
from django.contrib.auth.models import User
from appFive.models import UserProfileInfo  # Import your User model


# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
# class UserSignUpForm(forms.Form):
#     class Meta:
#         model = User 
#         fields = ['username','email', 'password']
#         widgets =  {
#             'password':forms.PasswordInput(),
#         }

# class YourFormName(forms.ModelForm):
#     class Meta:
#         model = YourModel  # Replace 'YourModel' with your actual model name
#         fields = ['username','email', 'password']
#         widgets =  {
#             'password':forms.PasswordInput(),
#         }