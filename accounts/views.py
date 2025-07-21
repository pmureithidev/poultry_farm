from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard(request):
    return render(
        request,
        'accounts/dashboard.html',
        {'section':'dashboard'}
    )

# user registration
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'