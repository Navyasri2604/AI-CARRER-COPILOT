from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'target_role', 'current_role', 'experience_level', 'phone', 'location', 'preferred_location', 'education', 'skills', 'bio', 'github_url', 'linkedin_url', 'portfolio_url', 'profile_picture')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'A short summary about your career direction...'}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.TextInput(attrs={'placeholder': 'Python, SQL, Django'}),
        }

    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email
        self.fields['skills'].initial = ', '.join(self.instance.skills or [])

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.skills = [skill.strip() for skill in str(self.cleaned_data.get('skills', '')).split(',') if skill.strip()] if isinstance(self.cleaned_data.get('skills'), str) else self.cleaned_data.get('skills', [])
        profile.user.email = self.cleaned_data.get('email', profile.user.email)
        if commit:
            profile.save()
            profile.user.save(update_fields=['email'])
        return profile
