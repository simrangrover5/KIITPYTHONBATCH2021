from django import forms 

class Register(forms.Form): # inheriting the Form class
    first_name = forms.CharField() # CharField --> type, first_name --> name + label tag
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class Login(forms.Form): # inheriting the Form class
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class GetEmail(forms.Form):
    email = forms.EmailField(label="Enter Your Email")
# <input type='text' name='fname'>