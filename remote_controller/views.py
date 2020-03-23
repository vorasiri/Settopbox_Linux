from django.shortcuts import render
from remote_controller.models import StateHolder

# Create your views here.
def home(request):
    state = StateHolder.objects.all()[0]
    if request.method == "POST":
        pass
    else:
        if request.GET.get('pills'):
            mode = request.GET.get('pills')
            if mode == 'full':
                state.controlDegree = 2
            elif mode == 'semi':
                state.controlDegree = 1
            else:
                state.controlDegree = 0
            state.save()
    return render(request, 'home.html', {'StateHolder': StateHolder.objects.all()[0]})