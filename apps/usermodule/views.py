from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages

def homePage(request):
    return render(request, 'usermodule/index.html')

def registerUser(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            messages.success(request, 'Successfully registered!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'usermodule/register.html', {'form': form})

def loginUser(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)

            return redirect('index')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'usermodule/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')