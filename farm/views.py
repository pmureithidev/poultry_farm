from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateFlockForm
from .models import Flock

# Create your views here.
@login_required
def dashboard(request):
   return render(
        request,
        'farm/dashboard.html',
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
                    'farm/farm.html',
                    {'form':form}
    )