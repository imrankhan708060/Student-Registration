from django.contrib.auth import authenticate,get_user_model
from django import forms

#Fetch model
User=get_user_model()


#Customize Login Form
class UserLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    
    #Overwrite the clean method
    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("please enter valid username and password")
            if not user.check_password(password):
                raise forms.ValidationError("please enter valid password")
            if not user.is_active:
                raise forms.ValidationError("user is not active user")
        return super().clean(*args,**kwargs)

#Customize SignUp Form
class UserSignUp(forms.ModelForm):
    email=forms.EmailField(label="Email")
    email2=forms.EmailField(label="Email")
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=("username","email","email2","password")
   
    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get("email")
        email2=self.cleaned_data.get("email2")
        if email!=email2:
            raise forms.ValidationError("please enter same email for both email fields")
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return super().clean(*args,**kwargs)




