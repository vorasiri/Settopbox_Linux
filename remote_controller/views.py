from django.shortcuts import render
from remote_controller.models import StateHolder

# Create your views here.
def home(request):
    if request.method == "POST":
        pass
    
    return render(request, 'home.html', {'StateHolder': StateHolder.objects.all()[0]})