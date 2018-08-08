from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import UserProfile



class RegeistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        )
    def save(self,commit=True):
        user=super(RegeistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()
        return user
class EditProfileForm(UserChangeForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=UserProfile
        fields=(
            'email',
            'description',
            'city',
            'website',
            'phoneno',
            'password',
        )
    def save(self,commit=True):
        user=super(EditProfileForm,self).save(commit=False)
        userprofile=user.userprofile
        userprofile.description=self.cleaned_data['description']
        userprofile.city=self.cleaned_data['city']
        userprofile.website=self.cleaned_data['website']
        userprofile.phoneno=self.cleaned_data['phoneno']
        user.email=self.cleaned_data['email']
        if commit:
            userprofile.save()
            user.save()
        return user
