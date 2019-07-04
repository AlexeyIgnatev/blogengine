from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import *


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()

        return render(request, 'user/register.html', context={'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('my_profile_url')
        else:
            try:
                form.errors['password'] = form.errors['password2']
                del form.errors['password2']
            except KeyError:
                pass
            return render(request, 'user/register.html', context={'form': form})


class ProfileView(View):
    def get(self, request, username=None):
        if username is None:
            return render(request, 'user/profile.html')
        else:
            user = get_object_or_404(User, username=username)
            return render(request, 'user/profile.html', context={'user': user})


class LogoutView(View):
    def get(self, request):
        return render(request, 'user/logout.html')

    def post(self, request):
        logout(request)
        return redirect('posts_list_url', permanent=True)


class ProfileEditView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        print(profile_form.fields)
        return render(request, 'user/profile_edit_form.html', context={
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('my_profile_url')
        return render(request, 'user/profile_edit_form.html', context={
            'user_form': user_form,
            'profile_form': profile_form
        })
