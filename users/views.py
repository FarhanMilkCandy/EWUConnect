from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import LoginForm, RegistrationForm
from users.models import ProfileModel, UserModel


def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('home')
            else:
                return redirect('login')
        else:
            return render(request, 'users/login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            ProfileModel.objects.create(user=user)
            # send_registration_mail(user)
            return redirect('home')
        else:
            return render(request, 'users/Registration.html', {"form": form})

    form = RegistrationForm()
    context = {
        "form": form
    }
    return render(request, 'users/Registration.html', context)


@login_required(login_url='login')
def profile_view(request, pk):
    user = UserModel.objects.get(id=pk)
    profile = ProfileModel.objects.get(user=user)
    is_self = False
    if user == request.user:
        is_self = True
    context = {
        'profile': profile,
        'is_self': is_self,
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def edit_profile_view(request):
    return render(request, 'users/edit-profile.html')


@login_required(login_url='login')
def account_settings_view(request):
    pass


def about_view(request):
    pass


def contact_view(request):
    pass
