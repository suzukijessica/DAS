from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Band, Member
from .forms import BandContactForm

def home(request):
    return render(request, 'home.html')

def band_listing(request):
    bands = Band.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        bands = bands.filter(name__icontains=var_get_search)
    return render(request, 'bands/band_listing.html', {'bands': bands})

def band_contact(request):
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})

@login_required(login_url='/accounts/login/')
def protected_view(request):
    return render(request, 'bands/protected.html', {'current_user': request.user})

def message(request):
    return HttpResponse('Access denied!')
