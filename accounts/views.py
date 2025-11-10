from django.shortcuts import render, redirect
from .forms import CustomSignUpForm


# user registration
def register(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomSignUpForm()
    return render(request, 'accounts/register.html', {'form': form})