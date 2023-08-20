from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django.contrib.auth.models import User
from .models import userBankAccount,userAddress


class userRegisterForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model : User
        field : ['userName','Password','reType-Password','firstName','lastName',
                 'email','account_type','gender','postal_code','country'
                 ]
        
    def self(self,commit = True):
        our_user = super().save(commit = False)
        if commit == True :
            our_user.save()
            account_type = self.cleaned_data.get('account_type ')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            country = self.cleaned_data.get('country')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            
            userAddress.objects.create (
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
                
            )
            
            userBankAccount.objects.create(
                user = our_user,
                account_type = account_type,
                birth_date = birth_date,
                gender = gender,
                account_no = 100000+ our_user.id
                )
            
         