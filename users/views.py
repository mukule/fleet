from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from .decorators import user_not_authenticated


# Create your views here.
def index(request):

    return render(request, 'users/index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "users/register.html",
        context={"form": form}
        )


@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("main:dashboard")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/index.html",
        context={"form": form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def clients(request):
    clients_list = Client.objects.all()  # Retrieve all Client objects from the database
    return render(request, 'users/clients.html', {'clients_list': clients_list})



def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully!')
            return redirect('users:clients')  # Replace 'clients_list' with the URL name for the clients list view
        else:
            messages.error(request, 'Error: Please correct the form errors.')
    else:
        form = ClientForm()
    return render(request, 'users/add_client.html', {'form': form})