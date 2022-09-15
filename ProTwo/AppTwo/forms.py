from django import forms
from AppTwo.models import Book
from django.contrib.auth.models import User
from AppTwo.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

#class FormAddBook(forms.Form):
#instead of calling forms.Form we use forms.ModelForm

class FormAddBook(forms.ModelForm):

    #Here you will add any validations if it is present

    class Meta:
        model = Book
        fields = '__all__'

class FormDeleteBook(forms.ModelForm):

    #Here you will add any validations if it is present

    class Meta:
        model = Book
        fields = ['book_name']

    # book_name = forms.CharField(max_length=100)
    # author_name = forms.CharField(max_length=100)
    # book_summary = forms.CharField(widget=forms.Textarea)
    # email = forms.EmailField(max_length=254,unique=True)
    # pswd = forms.CharField(max_length=30)
