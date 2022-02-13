from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# new
from .models import Resident
# new
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView
)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username} 🎉 ')
            return redirect('users')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f' Votre compte a été mis à jour ')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }

    return render(request, 'users/profile.html', context)


# NEW Resident List View
@login_required
class ResidentListView(ListView):
    model = Resident
    template_name = "users/residents.html"
    context_object_name = "residents"
    paginate_by = 5
    ordering = ['last_name']


# NEW Resident detail View
@login_required
class ResidentDetailView(DetailView):
    model = Resident


# NEW User List View
@login_required
class UserListView(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"
    paginate_by = 5
    ordering = ['last_name']

