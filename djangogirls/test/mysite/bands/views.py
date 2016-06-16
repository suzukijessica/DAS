from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Band, Member
from .forms import BandContactForm

def home(request):
    return render(request, 'home.html')

def band_listing(request):
    """ A view of all bands. """
    bands = Band.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        bands = bands.filter(name__icontains=var_get_search)
    return render(request, 'bands/band_listing.html', {'bands': bands})

def band_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = BandContactForm(request.POST)
    else:
        form = BandContactForm()
    return render(request, 'bands/band_contact.html', {'form': form})

@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bands/protected.html', {'current_user': request.user})

def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
