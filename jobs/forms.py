from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job, Application


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('employer', 'Employer'),
        ('applicant', 'Applicant'),
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='I am a:')
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Store user type in session for later use
            self.user_type = self.cleaned_data['user_type']
        return user


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
        } 