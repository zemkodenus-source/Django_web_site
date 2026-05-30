from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

@login_required
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST ,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/user_update.html', {'form': form})