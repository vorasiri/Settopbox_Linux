from django.shortcuts import render,HttpResponseRedirect
from remote_controller.models import StateHolder
from django.core.files.storage import FileSystemStorage
import os

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

        if request.FILES.get('inputGroupFile01',False):
            myfile = request.FILES['inputGroupFile01']
            fs = FileSystemStorage(location = '/home/kong/djangoProject/Settopbox_Linux/torrentFiles/')
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            if '.torrent' in filename:
                os.system("transmission-remote -n 'transmission:transmission' -a \'" + os.path.abspath('torrentFiles/'+filename) + "\'")
                print('start downloading: ' + filename)
            else:
                print('bad file')

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