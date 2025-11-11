from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateFlockForm
from .models import Flock

# Create your views here.
@login_required
def dashboard(request):
   return render(
        request,
        'farm/main_dashboard.html',
    )

@login_required
def flock_dashboard(request):
    flocks = Flock.objects.filter(user=request.user)
    return render(
        request,
        'farm/flock_dashboard.html',
        {'flocks': flocks}
    )

@login_required
def create_flock(request):
    if request.method == 'POST':
        form = CreateFlockForm(request.POST)
        if form.is_valid():
            flock = form.save(commit=False)
            flock.user = request.user
            flock.save()
            return redirect('create_flock')
    else:
        form = CreateFlockForm()

    return render(request,
                    'farm/create_flock_form.html',
                    {'form':form}
    )