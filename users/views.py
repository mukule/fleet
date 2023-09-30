from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.forms import ValidationError 

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
                return redirect("reservations:reservations")

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
    clients_list = Client.objects.all()
    return render(request, 'users/clients.html', {'clients_list': clients_list})


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Check license expiry date
            license_expiry = form.cleaned_data.get('license_expiry')
            if license_expiry and license_expiry < timezone.now().date():
                form.add_error('license_expiry', 'License has expired. Please enter a valid license expiry date.')
            else:
                form.save()
                messages.success(request, 'Client added successfully!')
                return redirect('users:clients')
        else:
            messages.error(request, 'Error: Please correct the form errors.')
    else:
        form = ClientForm()
    return render(request, 'users/add_client.html', {'form': form})


def edit_client(request, client_id):
    # Get the client object to be edited or return a 404 if it doesn't exist
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            client_name = f"{client.first_name} {client.last_name}"
            success_message = f'Client {client_name} updated successfully!'
            messages.success(request, success_message)
            return redirect('users:clients')
        else:
            messages.error(request, 'Error: Please correct the form errors.')
    else:
        # Populate the form with the current client data
        form = ClientForm(instance=client)

    return render(request, 'users/edit_client.html', {'form': form, 'client': client})