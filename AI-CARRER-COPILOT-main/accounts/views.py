from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import ProfileForm, RegisterForm
from .models import UserProfile

class CopilotLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        UserProfile.objects.create(user=user)
        login(request, user)
        messages.success(request, 'Welcome to your career copilot.')
        return redirect('dashboard')
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    profile_obj, _ = UserProfile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    return render(request, 'accounts/profile.html', {'form': form, 'profile_obj': profile_obj})

def logout_user(request):
    logout(request)
    return redirect('home')
