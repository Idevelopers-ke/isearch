from django.shortcuts import render
from .models import Destination
# Create your views here.
def home_page(request):

    dests = Destination.objects.all()

    return render(request, "hotels/index.html", {'dests': dests})