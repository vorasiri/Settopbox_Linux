from django.shortcuts import render,HttpResponseRedirect
from remote_controller.models import StateHolder

# Create your views here.
def home(request):
    state = StateHolder.objects.all()[0]
    if request.method == "POST":
        state.mediaSharing = 0
        state.homeEntertain = 0
        state.peer2peer = 0
        if request.POST.get('switchMedia'):
            state.mediaSharing = 1
        if request.POST.get('switchHomeEnt'):
            state.homeEntertain = 1
        if request.POST.get('switchP2P'):
            state.peer2peer = 1
        state.save()
        return HttpResponseRedirect('/')
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