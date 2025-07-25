from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomSignUpForm

# Create your views here.
@login_required
def dashboard(request):
    return render(
        request,
        'accounts/dashboard.html',
        {'section':'dashboard'}
    )

# user registration
def register(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomSignUpForm()
    return render(request, 'accounts/register.html', {'form': form})