from django.shortcuts import render
from teoapp.models import PostData
# Create your views here.
#from teoapp.tasks import hello

def index(request):
    listaWpisow = PostData.objects.all()
    return render(request, 'teoapp/index.html',  {'posts' : listaWpisow})
