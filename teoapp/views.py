from django.shortcuts import render
from teoapp.models import PostData, MyModel
# Create your views here.


def index(request):
    listaWpisow = PostData.objects.all()
    mymodels = MyModel.objects.all().order_by('-id')[:4] #zwraca cztery ostatnie obiekty z bazy danych
    return render(request, 'teoapp/index.html',  {'posts' : listaWpisow, 'mymodels' : mymodels})
