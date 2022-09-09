from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model 
from django.contrib.auth.views import PasswordResetView
# Create your views here.


class ResetPassword(PasswordResetView):
    def post(self, request, *args, **kwargs):
        if get_user_model().objects.filter(email=self.request.POST['email']):
            return super().post(request, *args, **kwargs)

        messages.warning(request, "User with this email does not exist")
        return redirect('password_reset')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')

            messages.success(
                request, f"Account have been created successfully for {name}")

            return redirect("index")

        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        print(error)
                        messages.error(request, error)

                return redirect('register')

    context = {

        'form': RegisterForm()
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            messages.success(
                request, f"{user.name}, You have successfully logged in")

            return redirect('index')

        else:
            messages.error(request, "invalid credentials")

            return redirect('login')

    context = {
        'form': LoginForm()
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, f'you have logged out succesfully')
        return redirect('login')
