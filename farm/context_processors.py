from django.db.models import Sum
from .models import Flock

# flock stats
def farm_stats(request):
    if request.user.is_authenticated:
        flocks = Flock.objects.filter(user=request.user)

        active_flocks = flocks.filter(is_active=True)
        active_count = active_flocks.count()

        inactive_flocks = flocks.filter(is_active=False)
        inactive_count = inactive_flocks.count()

        total_birds = active_flocks.aggregate(Sum('number_of_birds'))['number_of_birds__sum'] or 0
        total_layers = active_flocks.filter(flock_type='layers').aggregate(Sum('number_of_birds'))['number_of_birds__sum'] or 0
        total_broilers = active_flocks.filter(flock_type='broilers').aggregate(Sum('number_of_birds'))['number_of_birds__sum'] or 0
    
    else:
        # Define all values for anonymous users to avoid NameError
        active_count = 0
        inactive_count = 0
        total_birds = 0
        total_layers = 0
        total_broilers = 0
    
    return {
        'active_flocks': active_count,
        'inactive_flocks': inactive_count,
        'total_birds': total_birds,
        'total_layers': total_layers,
        'total_broilers':  total_broilers,
    }
