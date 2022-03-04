from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# new
from .models import Resident, Profile
# new
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView
)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Compte créé pour {username} 🎉 ')
#             return redirect('users')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


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
class ResidentListView(LoginRequiredMixin, ListView):
    model = Resident
    template_name = "users/residents.html"
    context_object_name = "residents"
    paginate_by = 5
    ordering = ['last_name']


# NEW User List View
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"
    paginate_by = 5
    ordering = ['last_name']


# NEW Relatives List View
class RelativeListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/relatives.html"
    context_object_name = "users"
    paginate_by = 5
    ordering = ['last_name']


# NEW Resident List View
class RelativeProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "users/relative_profiles.html"
    context_object_name = "relatives"
    paginate_by = 5
    ordering = ['last_name']

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('id'))
        relatives = user.profile.relatives.all()
        return relatives
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return Profile.objects.filter(relatives=user).order_by('-id')


# NEW Resident detail View
class ResidentDetailView(LoginRequiredMixin, DetailView):
    model = Resident

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = get_object_or_404(User, username=self.request.user.username)
        context['user_relatives_list'] = user.profile.relatives.all()
        return context
