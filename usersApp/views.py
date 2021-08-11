from django.shortcuts import render, redirect

#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from usersApp.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You may now be able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'usersApp/registration.html', {'form' : form})


    """ TYPES OF MESSAGES
    messages.debug
    messages.success
    messages.info
    messages.warning
    messages.error """

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You have updated your account successfully !')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'usersApp/profile.html', context)

